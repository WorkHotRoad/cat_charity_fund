from fastapi import FastAPI
from app.core.config import settings
# Импортируем настройки проекта из config.py.
# Импортируем роутер.
from app.api.routers import main_router


# Устанавливаем заголовок приложения при помощи аргумента title,
# в качестве значения указываем атрибут app_title объекта settings.
app = FastAPI(title=settings.app_title, description=settings.description)

# Подключаем роутер.
app.include_router(main_router)
