from functools import cache

from pydantic import BaseSettings, Field, HttpUrl


class Settings(BaseSettings):
    debug: bool = False

    # Add here more project configuration settings, as needed.

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@cache
def get_settings():
    return Settings()
