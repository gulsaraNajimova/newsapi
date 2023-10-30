from fastapi import APIRouter

from app.schemas.news_schema import SearchNews


news_router = APIRouter(
    prefix="/news",
    tags=["news"],
)

@news_router.get("/search-news/")
async def search_news(params: SearchNews):
    return {"news_found": params}

@news_router.get("/last-five-news")
async def get_last_5_news():
    pass

@news_router.get("/searched-news-today")
async def todays_searched_news_history():
    pass