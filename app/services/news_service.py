from app.repositories.news_repository import NewsRepository

class NewsService():
    def __init__(self, repository: NewsRepository) -> None:
        self.repository = repository

    def save_to_database(self, schema):
        return self.repository.save_to_database(schema)
    
    def get_last_five_news(self, owner_id: int):
        return self.repository.get_last_five_news(owner_id)
    
    def get_todays_searched_list(self, owner_id: int):
        return self.repository.get_todays_searched_list(owner_id)
    
    def delete_news_nextday(self):
        return self.repository.delete_news_nextday()