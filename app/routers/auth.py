from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from app.core.containers import Container
from app.core.dependencies import get_current_active_user
from app.models.users_model import UserModel
from app.schemas.auth_schema import SignInResponse, SignUpResponse, SignUpWithPassword, SignIn
from app.schemas.users_schema import User
from app.services.auth_service import AuthService


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@auth_router.post("/sign-up", response_model=SignUpResponse)
@inject
async def sign_up(user_info: SignUpWithPassword, service: AuthService = Depends(Provide[Container.auth_service])):
    return service.sign_up(user_info)

@auth_router.post("/sign-in", response_model=SignInResponse)
@inject
async def sign_in(user_info: SignIn, service: AuthService = Depends(Provide[Container.auth_service])):
    return service.sign_in(user_info)

@auth_router.get("/me", response_model=User)
async def get_me(current_user: UserModel = Depends(get_current_active_user)):
    return current_user