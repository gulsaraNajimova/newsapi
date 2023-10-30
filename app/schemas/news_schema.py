from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
import pydantic


class BaseNews(BaseModel):
    title: str
    author: str
    source: str
    description: str
    url: pydantic.AnyHttpUrl
    publishedAt: datetime


class PriorityType(str, Enum):
    EVERYTHING = "/everything"
    TOP_HEADLINES = "/top-headlines"

class SearchNews(BaseModel):
    keyword: Optional[List[str]]
    category: Optional[str]
    country: Optional[str]
    priority: PriorityType