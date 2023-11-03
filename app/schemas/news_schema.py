from datetime import datetime, date
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field
import pydantic

class SortBy(str, Enum):
    relevance = "relevance"
    popularity = "popularity"
    published_at = "publishedAt"
    none = ""

class SearchNews(BaseModel):
    q: Optional[str] = Field(default = "", description = "Keywords to look for")
    sources: Optional[str] = Field(default = "", description = "Sources to look for", max_length=20)
    from_: Optional[date] = Field(default = date.today())
    to_: Optional[date] = Field(default = date.today())
    sortBy: Optional[SortBy] = Field(default = SortBy.none, description = "Possible values: relevance, popularity, publishedAt")


class BaseNews(BaseModel):
    title: str
    author: str
    source: str
    description: str
    url: pydantic.AnyHttpUrl
    publishedAt: datetime
