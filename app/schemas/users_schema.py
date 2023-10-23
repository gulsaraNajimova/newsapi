from pydantic import BaseModel

class BaseUser(BaseModel):
    email: str
    username: str
    is_active: bool
    is_superuser: bool