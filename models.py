from pydantic import BaseModel

class EmailObservation(BaseModel):
    message: str

class EmailAction(BaseModel):
    action: str
