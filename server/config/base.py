import os

class Config:
    ENV = os.getenv("ENV", "development")
    DEBUG = ENV == "development"
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB uploads
