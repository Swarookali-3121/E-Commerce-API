import os
from dotenv import load_dotenv

load_dotenv()

class Environment():
    def __init__(self):
        self.DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:swaroop@localhost:5432/onlinestore")
        self.ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
        self.secret_key = os.environ.get("SECRET_KEY", "default_secret_key")
        self.ALGORITHM = os.environ.get("ALGORITHM", "HS256")
        self.INVALID_CREDENTIALS = "Invalid_Credentials"
        self.TOKEN_TYPE = "bearer"
        self.TOKEN_KEY = "token"

env = Environment()