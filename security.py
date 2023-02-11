# JWT Secret Key
import os

JWT_SECRET = os.getenv("JWT_SECRET", "secret_key")
JWT_ALGORITHM = "HS256"

