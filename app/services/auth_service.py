from datetime import timedelta
from app.core.config import configs
from app.core.exceptions import AuthError
from app.core.security import create_token, hash_password, verify_password
from app.models.users_model import UserModel
from app.schemas.auth_schema import Payload, SignIn, SignUpWithPassword
from app.services.user_service import UserService


def return_token(user_info):
    payload = Payload(
        id = user_info.id,
        email = user_info.email,
        username = user_info.username,
        is_superuser = user_info.is_superuser
    )

    token_lifespan = timedelta(minutes = configs.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token, expiration_datetime = create_token(payload.model_dump(), token_lifespan)  # noqa: E501
    result = {
        "access_token": access_token,
        "expiration": expiration_datetime,
        "user_info": user_info,
        }
    return result


class AuthService(UserService):
    def sign_up(self, user_info: SignUpWithPassword):
        get_hashed_password = hash_password(user_info.password)
        user = UserModel(
            email = user_info.email,
            hashed_password = get_hashed_password,
            username = user_info.username,
            is_active=True, 
            is_superuser=False)
        created_user = self.create_user(user)
        
        sign_up_result = return_token(created_user)
        return sign_up_result
    
    
    def sign_in(self, sign_in_info: SignIn):
        found_user = self.get_by_email(sign_in_info.email)
        if not found_user:
            raise AuthError("Incorrect email or password")
        if not verify_password(sign_in_info.password, found_user.hashed_password):
            raise AuthError("Incorrect email or password")
        if not found_user.is_active:
            raise AuthError("Account is not active")
        
        sign_in_result = return_token(found_user)
        return sign_in_result