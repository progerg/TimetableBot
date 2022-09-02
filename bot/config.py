from os import getenv
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("token")

DB_LOGIN = getenv("db_login")
DB_PASSWORD = getenv("db_password")
DB_NAME = getenv("db_name")
DB_HOST = getenv("db_host")
DB_PORT = getenv("db_port")
