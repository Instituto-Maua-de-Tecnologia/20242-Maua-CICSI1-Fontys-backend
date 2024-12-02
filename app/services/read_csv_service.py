import pandas as pd

class ReadCsvService:
    def __init__(self):
        pass
    
    def read(self):
        with open(self.file_path, 'r') as file:
            return file.read()