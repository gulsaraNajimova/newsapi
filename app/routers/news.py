from typing import Any
from fastapi import APIRouter, Depends

from app.schemas.news_schema import BaseNews, SearchNews


news_router = APIRouter(
    prefix="/news",
    tags=["news"],
)

@news_router.post("/")
async def news(news: BaseNews):
    return {"news": news}

@news_router.get("/search-news/{params}")
async def search_news(params: Any = Depends(SearchNews)):
    return {"news_found": params}