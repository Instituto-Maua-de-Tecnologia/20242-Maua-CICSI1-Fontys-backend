from fastapi import UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from app.services.user_services.upload_excel_service import UploadExcelService
from app.schemas.upload_excel import UploadExcelSchema  

class UploadExcelController:
    def __init__(self, service: UploadExcelService):
        self.service = service

    async def handle(self, file: UploadFile):
        try:
            upload_schema = UploadExcelSchema(file_name=file.filename)
        except ValidationError as e:
            raise HTTPException(status_code=400, detail=e.errors())

        if not file.filename.endswith(('.xls', '.xlsx')):
            raise HTTPException(status_code=400, detail="Invalid file format. Please upload an Excel file.")

        try:
            file_location = f"/tmp/{file.filename}"
            with open(file_location, "wb") as f:
                f.write(await file.read())

            json_data = self.service.execute(file_location)

            return JSONResponse(content={"data": json_data})

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")