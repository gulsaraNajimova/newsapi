from fastapi import APIRouter


news_router = APIRouter(
    prefix="/news",
    tags=["news"],
)