from idlelib.editor import keynames
from uuid import uuid4
from dotenv import load_dotenv, set_key
import os

def generate_and_save_api_key():
    load_dotenv()
    api_key = str(uuid4())
    print(f"Generated API Key: {api_key}")

    root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    env_file = os.path.join(root_directory, ".env")

    if not os.path.isfile(env_file):
        open(env_file, 'w').close()

    existing_key = os.getenv("API_KEYS", "")


    if not existing_key:
        set_key(env_file, "API_KEYS", api_key)
        print("API key saved to .env")
    else:
        # Append new key to existing comma-separated list
        new_value = existing_key + "," + api_key
        set_key(env_file, "API_KEYS", new_value)
        print("New API key added to .env")

    return api_key
