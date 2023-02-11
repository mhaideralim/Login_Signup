# Authenticate User and Generate JWT Token
from http.client import HTTPException

import jwt
from fastapi import Header
from database import user_collection
from security import JWT_SECRET, JWT_ALGORITHM


def authenticate_user(username: str, password: str):
    user = user_collection.find_one({"username": username, "password": password})
    if user:
        access_token = jwt.encode({"sub": username}, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return access_token
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password")


# Verify JWT Token
def verify_token(x_token: str = Header(None)):
    try:
        decoded_token = jwt.decode(x_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username = decoded_token["sub"]
        return username
    except jwt.PyJWTError:
        raise HTTPException(status_code=400, detail="Invalid token")

def authenticate_forgot_user(username: str):
    user = user_collection.find_one({"username": username})
    if user:
        access_token = jwt.encode({"sub": username}, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return access_token
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password")