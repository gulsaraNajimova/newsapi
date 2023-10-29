from typing import Any
from fastapi import APIRouter, Depends

from app.schemas.users_schema import BaseUser


user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@user_router.get("/")
async def get_users_list():
    pass

@user_router.get("/{user_id}")
async def get_user(user_id: int):
    pass

@user_router.patch("/{user_id}")
async def update_user(user_id: int,
    user_info: BaseUser):
    pass

@user_router.delete("/{user_id}")
async def delete_user(user_id: int):
    pass