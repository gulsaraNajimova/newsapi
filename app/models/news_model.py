from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class NewsModel(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    url = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner=relationship("UserModel", back_populates = "news")

    def __repr__(self):
        return f"<Title {self.title}, url {self.url}>"