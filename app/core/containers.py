from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database
from app.repositories.news_repository import NewsRepository
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.services.news_service import NewsService
from app.services.user_service import UserService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.routers.auth",
            "app.routers.news",
            "app.routers.users",
            "app.core.dependencies",
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DATABASE_URI)
        
    news_repository = providers.Factory(NewsRepository, session_factory=db.provided.session)  # noqa: E501
    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)  # noqa: E501
    
    auth_service = providers.Factory(AuthService, repository=user_repository)
    news_service = providers.Factory(NewsService, repository=news_repository)
    user_service = providers.Factory(UserService, repository=user_repository)

