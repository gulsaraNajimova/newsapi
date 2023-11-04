import requests

from app.repositories.news_repository import NewsRepository
from app.core.config import configs


API_KEY = configs.MY_NEWSAPI_KEY

class NewsService():
    def __init__(self, repository: NewsRepository) -> None:
        self.repository = repository

    def save_to_database(self, user_id: int, title, url):
        return self.repository.save_to_database(user_id, title, url)
    
    def get_last_five_news(self, owner_id: int):
        return self.repository.get_last_five_news(owner_id)
    
    def get_todays_view_history(self, owner_id: int):
        return self.repository.get_todays_view_history(owner_id)
    
    def delete_news_nextday(self):
        return self.repository.delete_news_nextday()
    

def get_everything(data):
    params = {"apiKey": API_KEY, **dict(data)}
    response_get = requests.get(url = "https://newsapi.org/v2/everything", params=params)
    return response_get.json()


def get_top_headlines(data):
    params = {"apiKey": API_KEY, **dict(data)}
    response_get = requests.get(url = "https://newsapi.org/v2/top-headlines", params=params)
    return response_get.json()