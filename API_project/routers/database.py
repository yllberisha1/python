import sqlite3
import os
from dotenv import load_dotenv

from API_project.main import DATABASE_URL
from main import connection

load_dotenv()
DATABASE_URL = os.getenv("DATABASE-URL")

def get_db_connection():
    connection = sqlite3.connect(DATABASE_URL)
    connection.row_factory = sqlite3.Row
    return connection