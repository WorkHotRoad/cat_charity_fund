from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'QRKot' # 'APP_TITLE'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db' # 'DATABASE_URL'
    description: str ='приложение для Благотворительного фонда поддержки котиков' # 'DESCRIPTION'
    secret: str = 'SECRET'

    class Config:
        env_file = './.env'


settings = Settings()
