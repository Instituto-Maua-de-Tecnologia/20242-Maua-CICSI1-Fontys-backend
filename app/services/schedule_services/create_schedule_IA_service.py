import google.generativeai as genai
from app.domain.entities.schedule_entity import ScheduleEntity
from app.core.config import settings
from sqlalchemy.orm import Session

from app.repositories.schedule_repository import ScheduleRepository

class CreateScheduleIAService:
    def __init__(self, db: Session):
        self.schedule_repository = ScheduleRepository(db)

    def generate_schedule(self, data: ScheduleEntity) -> ScheduleEntity:
        if not data:
            raise ValueError("The schedule data cannot be empty.")

        suggested_schedule_data = self._fetch_schedule_from_gemini(data)

        suggested_schedule = ScheduleEntity(**suggested_schedule_data)

        # Salvar o cronograma no banco de dados
        try:
            self.repository.create_schedule(suggested_schedule)
        except Exception as e:
            raise RuntimeError("Failed to save the suggested schedule to the database.") from e

        return suggested_schedule

    def _fetch_schedule_from_gemini(self, data: ScheduleEntity) -> dict:
        API_KEY = settings.API_KEY
        try:
            # Configura a chave da API do Gemini
            genai.configure(api_key=API_KEY)
            model = genai.GenerativeModel("gemini-1.5-flash")
            print(data.dict())
            # Envia um prompt personalizado com os dados do cronograma para a API
            prompt = f"Atue como um coordenador de curso com 20 anos de experiência, você agora deve desenvolver um cronograma de um curso de ciência da computação de 8 semestres, sendo que, a partir da metade do ano escolhida, você deve escolher os semestres impares ou pares, na primeira e segunda metades, respectivamente. Será enviado há você as disponibilidades e matérias lecionadas por cada professor. Tal como, os semestres das matérias. Você deve gerar o cronograma no seguinte formato: lista de json com os seguintes atributos user_id: string, name: string, subject_code: string, slot_id: number (1-54), day_of_week: string (Monday to Saturday), time: string (7h40, 9h30, 11h20, 13h10, 15h00, 16h50, 19h00, 20h50) availability_value: string (Possible, Impossible), subject_name: string, course_id: string, semester_number integer. Sendo cada um dos elementos da lista a representação de uma célula do cronograma, temos: slot_id: a coordenada da célula, determina dia e horário. Ela segue a direção vertical, e após terminar a coluna (um dia da semana), segue para o próximo. Ou seja, os ids caminham de horário para o horário. Ex.: 1 = monday, 7h40; 5 = monday, 15h00; 10 = tuesday, 9h30. availability_value: o quadro de disponibilidade de cada professor possui dois estados: Possible e Impossible. Você deve considerar apenas os dias os quais eles marcaram como Possible. A partir dessas informações, siga essas regras estritamente: você irá APENAS gerar o cronograma no formato estipulado. Você deve seguir essas normas preferenciais: Priorize usar os horários de manhã (7h40, 9h30, 11h20) e dias úteis da semana (segunda a sexta). Aqui estão as informações necessárias para a geração do cronograma: {data.dict()}"
            response = model.generate_content(prompt)
            
            # Verifica o sucesso da resposta
            if response.status_code != 200:
                raise RuntimeError("Failed to fetch schedule from Gemini AI")

            response_data = response.json()
        except Exception as e:
            raise RuntimeError(f"Error occurred while generating the schedule: {e}")

        return response_data
