from fastapi import APIRouter
from app.schemas.auth_schema import SignUpWithPassword


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@auth_router.post("/sign-up")
async def signup(user: SignUpWithPassword):
    return {"User Successfully created: ": user}