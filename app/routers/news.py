from typing import Any
from fastapi import APIRouter, Depends
from newsapi import NewsApiClient

from app.core.config import configs
from app.schemas.news_schema import SearchNews
from app.utils.news import get_everything


news_router = APIRouter(
    prefix="/news",
    tags=["news"],
)

@news_router.get("/get-all-news")
async def get_all_news(params: dict = Depends(SearchNews)):
    news = get_everything(params)
    return news


@news_router.get("/get-top-headlines")
async def get_top_headlines():
    pass


@news_router.get("/search-news/")
async def search_news(params: SearchNews):
    return {"news_found": params}

@news_router.get("/last-five-news")
async def get_last_5_news():
    pass

@news_router.get("/searched-news-today")
async def todays_searched_news_history():
    pass