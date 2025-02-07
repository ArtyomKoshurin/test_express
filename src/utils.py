import os

from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", default="random_url")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", default="random_key")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", default="random_alg")
JWT_ACCESS_COOKIE_NAME = os.getenv("JWT_ACCESS_COOKIE_NAME", default="random_name")
JWT_TOKEN_LOCATION = list(os.getenv("JWT_TOKEN_LOCATION", default="random_loc"))