from datetime import date
import json
from typing import Any
from fastapi import APIRouter, Depends
from app.core.containers import Container
from app.core.dependencies import get_current_user
from app.models.users_model import UserModel
from dependency_injector.wiring import Provide, inject

from app.schemas.news_schema import SaveNews, SearchEverything, SearchTopHeadlines
from app.services.news_service import NewsService
from app.utils.news import get_everything, get_top_headlines


news_router = APIRouter(
    prefix="/news",
    tags=["news"],
)

@news_router.get("/get-all-news")
async def get_all_news(params: Any = Depends(SearchEverything),
    current_user: UserModel = Depends(get_current_user)):
    news = get_everything(params)
    
    return news


@news_router.get("/get-top-headlines")
async def get_top_news(params: Any = Depends(SearchTopHeadlines),
    current_user: UserModel = Depends(get_current_user)):
    news = get_top_headlines(params)
    
    return news


@news_router.post("/save-view-history")
@inject
async def save_view_history(news_details: Any = Depends(SaveNews),
    current_user: UserModel = Depends(get_current_user),
    service: NewsService = Depends(Provide[Container.news_service])):
    
    return service.save_to_database(current_user.id, news_details.title, news_details.url)


@news_router.get("/last-five-news")
async def get_last_5_news():
    pass

@news_router.get("/searched-news-today")
async def todays_searched_news_history():
    pass