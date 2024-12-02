from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from sqlalchemy import select
import jwt
from jwt import algorithms
import requests
from app.models import User
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_microsoft_public_keys():
    response = requests.get("https://login.microsoftonline.com/common/discovery/v2.0/keys")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch Microsoft keys.")
    return response.json()["keys"]

@router.post("/auth")
def link_microsoft_account(
        name: str,
        authorization: str = Header(...),
        db: Session = Depends(get_db)
):
    print(f"Received authorization header: {authorization}")  # Debugging print statement

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid Authorization header.")

    access_token = authorization.split("Bearer ")[1]
    print(f"Received access token: {access_token}")  # Debugging print statement

    # Get Microsoft public keys
    keys = get_microsoft_public_keys()
    print(f"Microsoft public keys fetched: {keys}")  # Debugging print statement

    unverified_header = jwt.get_unverified_header(access_token)
    print(f"Unverified JWT header: {unverified_header}")  # Debugging print statement

    # Find the correct key based on 'kid'
    key = next((k for k in keys if k["kid"] == unverified_header["kid"]), None)
    if not key:
        raise HTTPException(status_code=401, detail="Invalid token.")

    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
    print(f"Public key used for decoding: {public_key}")  # Debugging print statement

    # Decode the JWT payload
    payload = jwt.decode(
        access_token,
        public_key,
        algorithms=["RS256"],
        audience="b55f918c-264c-437d-98ad-c7efd3afcdf4",
        issuer="https://login.microsoftonline.com/3953a2c3-4821-4818-ae33-a4c5bcc5fdfb/v2.0"
    )
    print(f"Decoded JWT payload: {payload}")  # Debugging print statement

    if payload.get("name") != name:
        raise HTTPException(status_code=401, detail="Token name mismatch.")

    # Query the user from the database using the name
    user = db.scalar(select(User).where(User.name.eq(name)))
    print(f"User found in database: {user}")  # Debugging print statement

    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    if not user.microsoft_id:
        user.microsoft_id = payload.get("sub")
        db.commit()
        db.refresh(user)

    # If user is already registered, return a message
    if user.status == "registered":
        return {"message": "User is already registered."}

    # Update user status to 'registered'
    user.status = "registered"
    db.commit()
    db.refresh(user)

    return {"message": "User successfully registered.", "name": name}
