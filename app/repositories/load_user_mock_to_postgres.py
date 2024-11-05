from app.db.session import get_db

def load_fake_user_to_postgres():
  try:
    db = get_db()

    user = {
      'user_id': '9d5c8d5b-e40b-4df1-8a8b-cf604b38b416',
      'microsoft_id': '9d5c8d5b-e40b-4df1-8a8b-cf604b38b417',
      'email': 'digao@gmail.com',
      'password': 'Teste123$',
      'name': 'Digao',
      'user_type': 'Professor',
      'notes': 'TESTEEEEEEEEEEE',
    }

    db.add(user)
    db.commit()
  except Exception as e:
    raise e  
  finally:
    db.close()

    