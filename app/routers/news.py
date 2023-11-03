from typing import Any
from fastapi import APIRouter, Depends

from app.schemas.news_schema import SearchEverything, SearchTopHeadlines
from app.utils.news import get_everything, get_top_headlines


news_router = APIRouter(
    prefix="/news",
    tags=["news"],
)

@news_router.get("/get-all-news")
async def get_all_news(params: Any = Depends(SearchEverything)):
    news = get_everything(params)
    return news


@news_router.get("/get-top-headlines")
async def get_top_news(params: Any = Depends(SearchTopHeadlines)):
    news = get_top_headlines(params)
    return news


@news_router.get("/last-five-news")
async def get_last_5_news():
    pass

@news_router.get("/searched-news-today")
async def todays_searched_news_history():
    pass