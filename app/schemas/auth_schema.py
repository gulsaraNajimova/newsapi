from pydantic import BaseModel
from datetime import datetime

from app.schemas.users_schema import BaseUser


class SignUp(BaseModel):
    email: str
    username: str

class SignUpWithPassword(SignUp):
    password: str

    class Config:
        from_attributes = True
        json_schema_extra={
            "example": {
                "email": "sarah@gmail.com",
                "password": "password123",
                "username": "sarah"
            }
        }

class Payload(BaseModel):
    id: int
    email: str
    username: str
    is_superuser: bool

class SignUpResponse(BaseModel):
    access_token: str
    expiration: datetime
    user_info: BaseUser


class SignIn(BaseModel):
    email: str
    password: str

class SignInResponse(SignUpResponse):
    ... 


