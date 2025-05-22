from fastapi import HTTPException, status

class NotFoundException(HTTPException):
    def __init__(self, detail: str = "O recurso solicitado não foi encontrado!"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)