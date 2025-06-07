from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    admin_email: str
    items_per_user: int = 50

settings = Settings(app_name="Myapp", admin_email="admin@example.com")
print(settings)
