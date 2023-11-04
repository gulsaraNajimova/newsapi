from dependency_injector.wiring import Provide, inject
from typing import List
from fastapi import APIRouter, Depends
from app.core.containers import Container
from app.core.dependencies import get_current_superuser, get_current_user
from app.core.exceptions import AuthError
from app.models.users_model import UserModel

from app.schemas.users_schema import BaseUser, EditUser, User
from app.services.user_service import UserService


user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)

# Only for superusers
@user_router.get("/get-users-list", response_model=List[BaseUser])
@inject
async def get_users_list(skip: int =0 , limit: int = 100, current_user: UserModel = Depends(get_current_superuser), 
    service: UserService = Depends(Provide[Container.user_service])
    ):
    return service.get_users_list(skip, limit)
    

@user_router.get("/get-user/{user_id}", response_model=BaseUser)
@inject
async def get_user(user_id: int, 
    current_user: UserModel = Depends(get_current_superuser),
    service: UserService = Depends(Provide[Container.user_service])
    ):
    return service.get_by_id(user_id)
    

@user_router.patch("/update-user-info", response_model=User)
@inject
async def update_user_info(user_info: EditUser, 
    current_user: UserModel = Depends(get_current_user),
    service: UserService = Depends(Provide[Container.user_service])
    ):
    return service.patch_user_info(current_user.id, user_info)

@user_router.delete("/delete-user")
@inject
async def delete_user(user_id:int,
    current_user: UserModel = Depends(get_current_user),
    service: UserService = Depends(Provide[Container.auth_service])
    ):

    if user_id == current_user.id or current_user.is_superuser:
        return service.delete_user(current_user.id)
    else: 
        return AuthError(f"Not authrorized to delete requested user with ID {user_id}")