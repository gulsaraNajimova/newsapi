import schedule
import time 
from fastapi import FastAPI

from app.core.database import engine, Base
from app.routers.auth import auth_router
from app.routers.news import news_router
from app.routers.users import user_router
from app.services.news_service import NewsService

app=FastAPI(
    title="News Aggregation API ",
    description="Discover the world's latest stories instantly with our News API app,\
        delivering real-time updates on diverse topics tailored to your interests",
    version="0.0.1",
    openapi_url="/https://newsapi//openapi.json"
)

Base.metadata.create_all(bind=engine) #creates database tables


app.include_router(auth_router)
app.include_router(news_router)
app.include_router(user_router)

# delete all rows from news table every day at 00:00 (12 a.m.)
schedule.every().day.at("00:00").do(NewsService.delete_news_nextday)

while True:
    schedule.run_pending()
    time.sleep(1)