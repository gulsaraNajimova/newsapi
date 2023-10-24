from typing import Any
from fastapi import APIRouter, Depends

from app.schemas.news_schema import SearchNews


news_router = APIRouter(
    prefix="/news",
    tags=["news"],
)

@news_router.get("/search-news/{params}")
async def search_news(params: Any = Depends(SearchNews)):
    return {"news_found": params}

@news_router.get("/last-five-news")
async def get_last_5_news():
    pass

@news_router.get("/search-list-today")
async def todays_search_list_history():
    pass