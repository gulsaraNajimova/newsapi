from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field
import pydantic

class SortBy(str, Enum):
    relevance = "relevance"
    popularity = "popularity"
    published_at = "publishedAt"
    none = ""

class SearchEverything(BaseModel):
    q: Optional[str] = Field(default = "", description = "Keywords or phrases to look for")
    sources: Optional[str] = Field(default = "", description = "Sources to look for", max_length=20)
    from_: Optional[date] = Field(default = date.today())
    to_: Optional[date] = Field(default = date.today())
    sortBy: Optional[SortBy] = Field(default = SortBy.none, description = "Possible values: relevance, popularity, publishedAt")


class SearchTopHeadlines(BaseModel):
    q: Optional[str] = Field(default = "", description = "Keywords or phrases to look for")
    sources: Optional[str] = Field(default = "", description = "Sources to look for", max_length=20)
    country: Optional[str] = Field(default = "us", description = "Write the 2-letter country code")
    category: Optional[str] = Field(default = "", description = "Possible options: business, entertainment, general health, science, sports, technology")

