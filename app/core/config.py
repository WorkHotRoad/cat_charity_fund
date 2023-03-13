from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'APP_TITLE'
    database_url: str = 'DATABASE_URL'
    description: str ='DESCRIPTION'
    secret: str = 'SECRET'

    class Config:
        env_file = './.env'


settings = Settings()
