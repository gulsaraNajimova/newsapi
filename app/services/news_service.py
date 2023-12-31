from app.repositories.news_repository import NewsRepository

class NewsService():
    def __init__(self, repository: NewsRepository) -> None:
        self.repository = repository

    def save_to_database(self, user_id: int, title, url):
        return self.repository.save_to_database(user_id, title, url)
    
    def get_last_five_news(self, owner_id: int):
        return self.repository.get_last_five_news(owner_id)
    
    def get_todays_view_history(self, owner_id: int):
        return self.repository.get_todays_view_history(owner_id)
    
