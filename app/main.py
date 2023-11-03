from fastapi import FastAPI

from app.core.config import configs
from app.core.containers import Container
from app.routers.auth import auth_router
from app.routers.news import news_router
from app.routers.users import user_router
from app.apscheduler.jobs import scheduler


class AppCreator:
    def __init__(self):
        self.app = FastAPI(
            title=configs.PROJECT_NAME,
            description="Discover the world's latest stories instantly with our News API app,\
                delivering real-time updates on diverse topics tailored to your interests",
            openapi_url=f"{configs.API}/openapi.json",
            version="0.0.1",
        )

        # set db and container
        self.container = Container()
        self.db = self.container.db()
        # self.db.create_database()

        # set routes
        @self.app.get("/")
        def root():
            return "service is working"

        self.app.include_router(auth_router)
        self.app.include_router(news_router)
        self.app.include_router(user_router)

app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container

scheduler.start()