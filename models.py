# User Login Request Body Model
from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str

