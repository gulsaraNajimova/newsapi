from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError

from app.core.exceptions import DuplicatedError, NotFoundError
from app.core.security import hash_password
from app.models.users_model import UserModel

class UserRepository:
    def __init__(self, 
    session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory
        self.user_model = UserModel

    def create_user(self, schema):
        with self.session_factory() as session:
            print(vars(schema))
            query = self.user_model(
                email = schema.email,
                hashed_password = schema.hashed_password,
                username = schema.username,
                is_active = schema.is_active,
                is_superuser = schema.is_superuser
            )
            try:
                session.add(query)
                session.commit()
                session.refresh(query)
            except IntegrityError as e:
                raise DuplicatedError(str(e.orig))
            return query
        
    def get_by_id(self, user_id: int, eager = False):
        with self.session_factory() as session:
            query = session.query(self.user_model)
            if eager:
                for eager in getattr(self.user_model, "eagers", []):
                    query = query.options(joinedload(getattr(self.user_model, eager)))
            query = query.filter(self.user_model.id == user_id).first()
            if not query:
                raise NotFoundError(f"ID not found: {user_id}")
            return query
        
    def get_by_email(self, email: str):
        with self.session_factory() as session:
            return session.query(self.user_model).filter(self.user_model.email==email).first()  # noqa: E501
        
    def get_users_list(self, skip: int, limit: int):
        with self.session_factory() as session:
            return session.query(self.user_model).offset(skip).limit(limit).all()

        
    def update_user_info(self, user_id: int, schema):
        with self.session_factory() as session:
            if 'hashed_password' in schema.dict(exclude_unset=True):
                hashed_password = hash_password(schema.hashed_password)
                schema.hashed_password = hashed_password

            update_dict = schema.dict(exclude_unset=True)
            print("Update Dictionary:", update_dict) 

            session.query(self.user_model).filter(self.user_model.id == user_id).update(update_dict)
            session.commit()
            return self.get_by_id(user_id)
        
    def delete_user(self, user_id: int):
        with self.session_factory() as session:
            query = session.query(self.user_model).filter(self.user_model.id == user_id).first()  # noqa: E501
            if not query:
                raise NotFoundError(f"ID not found: {user_id}")
            session.delete(query)
            session.commit()

            

