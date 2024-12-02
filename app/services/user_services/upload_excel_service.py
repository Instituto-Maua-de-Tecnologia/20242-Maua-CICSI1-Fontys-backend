import pandas as pd

class UploadExcelService:
    def __init__(self):
        pass

    def execute(self, file_path: str):
        try:
            df = pd.read_excel(file_path)

            if 'PROFESSOR' not in df.columns:
                raise Exception("The column 'PROFESSOR' does not exist in the Excel file.")

            unique_professors = df['PROFESSOR'].drop_duplicates()

            json_data = unique_professors.to_list() 
            return {"professores": json_data}
        except Exception as e:
            raise Exception(f"Failed to process Excel file: {str(e)}")
