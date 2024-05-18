from fastapi import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from passlib.hash import argon2

from app.core.config import configs
from app.core.exceptions import AuthError


ALGORITHM = "HS256"


# Create Token
def create_token(payload_data: dict, expires_delta: Optional[timedelta] = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        access_token_expires = timedelta(minutes=configs.ACCESS_TOKEN_EXPIRE_MINUTES)
        expire = datetime.utcnow() + access_token_expires
    payload = {"exp": expire, **payload_data}
    encoded_jwt = jwt.encode(payload, configs.SECRET_KEY, algorithm=ALGORITHM)
    expiration_datetime = expire.strftime(configs.DATETIME_FORMAT)
    return encoded_jwt, expiration_datetime


def hash_password(password: str):
    password_bytes = password.encode('utf-8')
    return argon2.hash(password_bytes)


def verify_password(plain_password, hashed_password):
    plain_password_bytes = plain_password.encode('utf-8')
    return argon2.verify(plain_password_bytes, hashed_password)


def decode_jwt(token: str):
    try:
        decoded_token = jwt.decode(token, configs.SECRET_KEY, algorithms=ALGORITHM)
        return decoded_token if decoded_token["exp"] >= int(
            round(datetime.utcnow().timestamp())
            ) else None

    except Exception as e:  # noqa: F841
        return {}


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self).__call__(request)
            
        if credentials:
            if not credentials.scheme == "Bearer":
                raise AuthError(detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise AuthError(detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise AuthError(detail="Invalid authorization code.")
        

    def verify_jwt(self, jwt_token: str):
        is_token_valid: bool = False
        try:
            payload = decode_jwt(jwt_token)
        except Exception as e:  # noqa: F841
            payload = None
        if payload:
            is_token_valid = True
        return is_token_valid
