import requests
from app.core.config import configs

API_KEY = configs.MY_NEWSAPI_KEY

def get_everything(data):
    params = {"apiKey": API_KEY, **dict(data)}
    response_get = requests.get(url = "https://newsapi.org/v2/everything", params=params)
    return response_get.json()


def get_top_headlines(data):
    params = {"apiKey": API_KEY, **dict(data)}
    response_get = requests.get(url = "https://newsapi.org/v2/top-headlines", params=params)
    return response_get.json()