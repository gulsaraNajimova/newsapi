from pydantic import BaseModel

class BaseUser(BaseModel):
    email: str
    hashed_password: str
    username: str
    is_active: bool
    is_superuser: bool

class User(BaseUser):
    id: int