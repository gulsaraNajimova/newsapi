from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def create_user(self, schema):
        return self.repository.create_user(schema)
    
    def get_by_id(self, user_id: int):
        return self.repository.get_by_id(user_id)
    
    def get_by_email(self, email: str):
        return self.repository.get_by_email(email)
    
    def get_users_list(self, skip: int, limit: int):
        return self.repository.get_users_list(skip, limit)
    
    def patch_user_info(self, user_id: int, schema):
        return self.repository.update_user_info(user_id, schema)
    
    def delete_user(self, user_id: int):
        return self.repository.delete_user(user_id)