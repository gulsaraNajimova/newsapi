from dependency_injector.wiring import Provide, inject
from typing import Any, List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from app.core.containers import Container
from app.core.dependencies import get_current_superuser
from app.models.users_model import UserModel

from app.schemas.users_schema import BaseUser
from app.services.user_service import UserService


user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)

# Only for superusers
@user_router.get("/", response_model=List[BaseUser])
@inject
async def get_users_list(skip: int =0 , limit: int = 100, current_user: UserModel = Depends(get_current_superuser), 
    service: UserService = Depends(Provide[Container.user_service])
    ):
    users_list = service.get_users_list(skip, limit)
    return jsonable_encoder(users_list)
    

@user_router.get("/{user_id}", response_model=BaseUser)
@inject
async def get_user(user_id: int, 
    current_user: UserModel = Depends(get_current_superuser),
    service: UserService = Depends(Provide[Container.user_service])
    ):
    return service.get_by_id(user_id)
    

@user_router.patch("/{user_id}")
async def update_user(user_id: int,
    user_info: BaseUser):
    pass

@user_router.delete("/{user_id}")
async def delete_user(user_id: int):
    pass