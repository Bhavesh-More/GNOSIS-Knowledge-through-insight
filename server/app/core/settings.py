from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    ENV: str

    class Config:
        env_file = ".env"

settings = Settings()
