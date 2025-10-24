import os
from dotenv import load_dotenv
load_dotenv()

DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_NAME = os.getenv("POSTGRES_DB", "students_db")

# Detectar si estamos en Docker
if os.getenv("DOCKER_ENV") == "1":
    DB_HOST = os.getenv("POSTGRES_HOST", "db")
else:
    DB_HOST = os.getenv("POSTGRES_HOST", "localhost")

SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
