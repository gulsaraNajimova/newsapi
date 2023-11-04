from contextlib import AbstractContextManager
from typing import Callable, List
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.news_model import NewsModel

class NewsRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        self.news_model = NewsModel

    def save_to_database(self, user_id: int, title, url):
        with self.session_factory() as session:
            query = self.news_model(
                title = title,
                url = url,
                owner_id = user_id
            )
            session.add(query)
            session.commit()
            session.refresh(query)
            return query
        
    def get_last_five_news(self, owner_id: int) -> List:
        with self.session_factory() as session:
            return session.query(self.news_model)\
                .filter(self.news_model.owner_id == owner_id)\
                .order_by(desc(self.news_model.id)).limit(5).all()
        
    def get_todays_searched_list(self, owner_id: int) -> List:
        with self.session_factory() as session:
            return session.query(self.news_model)\
                .filter(self.news_model.owner_id == owner_id).all()
