from typing import Optional
from pydantic import BaseModel

class BaseUser(BaseModel):
    email: str
    hashed_password: str
    username: str
    is_active: bool
    is_superuser: bool

class User(BaseUser):
    id: int

class EditUser(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    username: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None