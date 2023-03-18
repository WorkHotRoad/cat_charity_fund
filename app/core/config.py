from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'QRKot'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    description: str = 'приложение для Благотворительного фонда поддержки котиков'
    secret: str = 'SECRET'

    class Config:
        env_file = './.env'


settings = Settings()
