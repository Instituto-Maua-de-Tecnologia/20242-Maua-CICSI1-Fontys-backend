from pydantic import BaseModel, Field

class UploadExcelSchema(BaseModel):
    file_name: str = Field(..., description="The name of the Excel file being uploaded.")
