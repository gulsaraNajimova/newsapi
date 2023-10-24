from typing import Any
from fastapi import APIRouter, Depends
from app.schemas.auth_schema import SignUpWithPassword, SignIn


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@auth_router.post("/sign-up")
async def sign_up(user_info: Any = Depends(SignUpWithPassword)):
    return {"User successfully created: ": user_info}

@auth_router.post("/sign-in")
async def sign_in(user_info: Any = Depends(SignIn)):
    return {"User successfully signed in": user_info}

@auth_router.get("/me")
async def get_me():
    pass