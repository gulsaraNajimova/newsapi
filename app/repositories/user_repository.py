from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError

from app.core.exceptions import DuplicatedError, NotFoundError
from app.models.users_model import UserModel

class UserRepository:
    def __init__(self, 
    session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        self.user_model = UserModel

    def create_user(self, schema):
        with self.session_factory() as session:
            query = self.user_model(**schema.dict())
            try:
                session.add(query)
                session.commit()
                session.refresh(query)
            except IntegrityError as e:
                raise DuplicatedError(str(e.orig))
            return query
        
    def get_by_id(self, user_id: int, eager = False):
        with self.session_factory as session:
            query = session.query(self.user_model)
            if eager:
                for eager in getattr(self.user_model, "eagers", []):
                    query = query.options(joinedload(getattr(self.user_model, eager)))
            query = query.filter(self.user_model.id == user_id).first()
            if not query:
                raise NotFoundError(f"ID not found: {user_id}")
            return query
        
    def get_users_list(self, skip: int, limit: int):
        with self.session_factory as session:
            session.query(self.user_model).offset(skip).limit(limit).all()
        
    def update_user_info(self, user_id: int, schema):
        with self.session_factory as session:
            session.query(self.user_model).filter(self.user_model.id == user_id)\
                .update(schema.dict(exclude_none=True))
            session.commit()
            return self.get_by_id(user_id)
        
    def delete_user(self, user_id: int):
        with self.session_factory as session:
            query = session.query(self.user_model)\
                .filter(self.user_model.id == user_id).first()
            if not query:
                raise NotFoundError(f"ID not found: {user_id}")
            session.delete(query)
            session.commit()

            

