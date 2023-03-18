from fastapi import FastAPI
from app.core.config import settings
# Импортируем настройки проекта из config.py.
# Импортируем роутер.
from app.api.routers import main_router


app = FastAPI(title=settings.app_title, description=settings.description)

app.include_router(main_router)
