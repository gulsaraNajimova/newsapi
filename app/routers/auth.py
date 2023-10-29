from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from app.core.containers import Container
from app.schemas.auth_schema import SignUpResponse, SignUpWithPassword, SignIn
from app.services.auth_service import AuthService


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@auth_router.post("/sign-up", response_model=SignUpResponse)
@inject
async def sign_up(user_info: SignUpWithPassword, service: AuthService = Depends(Provide[Container.auth_service])):
    return service.sign_up(user_info)

@auth_router.post("/sign-in")
async def sign_in(user_info: SignIn):
    return {"User successfully signed in": user_info}

@auth_router.get("/me")
async def get_me():
    pass