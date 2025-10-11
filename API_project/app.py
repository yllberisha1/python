import streamlit as st
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")

def get_categories():
    response = requests.get(f"{API_BASE_URL}/categories/")
    response.raise_for_status()
    return response.json()

def get_recipes(cuisine=None, difficulty=None):
    params = {}
    if cuisine:
        params['cuisine'] = cuisine
    if difficulty:
        params['difficulty'] = difficulty
    response = requests.get(f"{API_BASE_URL}/recipes/", params=params)
    response.raise_for_status()
    return response.json()

def create_category(category_name):
    response = requests.post(f"{API_BASE_URL}/categories/", json={"name": category_name})
    response.raise_for_status()
    return response.json()

def update_category(category_id, new_name):
    response = requests.put(f"{API_BASE_URL}/categories/{category_id}/", json={"name": new_name})
    response.raise_for_status()
    return response.json()

def delete_category(category_id):
    response = requests.delete(f"{API_BASE_URL}/categories/{category_id}/")
    response.raise_for_status()
    return response.status_code == 204  # typically no content on successful delete

def create_recipe(recipe_name, description, ingredients, instructions, cuisine, difficulty, category_id):
    data = {
        "name": recipe_name,
        "description": description,
        "ingredients": ingredients,
        "instructions": instructions,
        "cuisine": cuisine,
        "difficulty": difficulty,
        "category_id": category_id
    }
    response = requests.post(f"{API_BASE_URL}/recipes/", json=data)
    response.raise_for_status()
    return response.json()

def update_recipe(recipe_id, recipe_name, description, ingredients, instructions, cuisine, difficulty, category_id):
    data = {
        "name": recipe_name,
        "description": description,
        "ingredients": ingredients,
        "instructions": instructions,
        "cuisine": cuisine,
        "difficulty": difficulty,
        "category_id": category_id
    }
    response = requests.put(f"{API_BASE_URL}/recipes/{recipe_id}/", json=data)
    response.raise_for_status()
    return response.json()
