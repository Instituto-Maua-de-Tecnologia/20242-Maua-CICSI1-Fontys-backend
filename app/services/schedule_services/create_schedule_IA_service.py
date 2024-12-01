import google.generativeai as genai
from app.domain.entities.schedule_entity import ScheduleEntity
from app.domain.interfaces.repositories.schedule_repository_interface import IScheduleRepository
from app.core.config import settings

class CreateScheduleIAService:
    def __init__(self, repository: IScheduleRepository):
        self.repository = repository

    def generate_schedule(self, data: ScheduleEntity) -> ScheduleEntity:
        """
        Gera um cronograma utilizando a API Gemini AI e salva no banco de dados.

        :param data: Instância de ScheduleEntity com os dados iniciais do cronograma.
        :return: Cronograma gerado e salvo no banco de dados.
        """
        # Validação básica
        if not data:
            raise ValueError("The schedule data cannot be empty.")
        
        # Obter o cronograma sugerido da API Gemini AI
        suggested_schedule_data = self._fetch_schedule_from_gemini(data)

        # Criar a entidade do cronograma sugerido
        suggested_schedule = ScheduleEntity(**suggested_schedule_data)

        # Salvar o cronograma no banco de dados
        try:
            self.repository.create_schedule(suggested_schedule)
        except Exception as e:
            raise RuntimeError("Failed to save the suggested schedule to the database.") from e

        return suggested_schedule

    def _fetch_schedule_from_gemini(self, data: ScheduleEntity) -> dict:
        """
        Utiliza a API Gemini AI para obter sugestões de cronograma com base nos dados fornecidos.

        :param data: Dados do cronograma a ser gerado.
        :return: Dados do cronograma sugerido pela API.
        """
        API_KEY = settings.API_KEY
        try:
            # Configura a chave da API do Gemini
            genai.configure(api_key=API_KEY)
            model = genai.GenerativeModel("gemini-1.5-flash")
            print(data.dict())
            # Envia um prompt personalizado com os dados do cronograma para a API
            prompt = f"Gere um cronograma com os seguintes detalhes, alterando apenas : {data.dict()}"
            response = model.generate_content(prompt)
            
            # Verifica o sucesso da resposta
            if response.status_code != 200:
                raise RuntimeError("Failed to fetch schedule from Gemini AI")

            response_data = response.json()
        except Exception as e:
            raise RuntimeError(f"Error occurred while generating the schedule: {e}")

        return response_data
