from fastapi import FastAPI
from routers import recipes, categories
from dotenv import load_dotenv
import os
from database import get_db_connection

# Load environment variables
load_dotenv()

# Get the database URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Initialize the FastAPI app
app = FastAPI()

# Include routers
app.include_router(categories.router)
app.include_router(recipes.router)

# Startup event to initialize the database
@app.on_event("startup")
def start_up():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            ingredients TEXT,
            instruction TEXT,
            cuisine TEXT,
            difficulty TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')

    conn.commit()
    conn.close()

# Root endpoint
@app.get('/')
def read_root():
    return {"message": "FastAPI wit hSQLite project"}
