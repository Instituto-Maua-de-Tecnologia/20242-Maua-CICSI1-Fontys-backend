from app.shared.helpers.errors.base_errors import BaseError


class EntityError(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Field {message} is not valid')

class EntityParameterTypeError(EntityError):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class EntityParameterError(EntityError):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class WrongEntityError(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Field {message} is not equal')