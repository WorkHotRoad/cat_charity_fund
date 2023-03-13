from sqlalchemy import Column, DateTime, Integer, String, Integer, Boolean
from datetime import datetime
from app.core.db import Base

class CharityProject(Base):
    name = Column(String(100), unique=True, nullable=False) # уникальное название проекта, обязательное строковое поле; допустимая длина строки — от 1 до 100 символов включительно;
    description = Column(String(100), nullable=False) # описание, обязательное поле, текст; не менее одного символа;
    full_amount = Column(Integer, min=1, nullable=False)# требуемая сумма, целочисленное поле; больше 0;
    invested_amount = Column(Integer, default=0)  # внесённая сумма, целочисленное поле; значение по умолчанию — 0;
    fully_invested = Column(Boolean(), default=False) # булево значение, указывающее на то, собрана ли нужная сумма для проекта (закрыт ли проект); значение по умолчанию — False;
    create_date = Column(DateTime, default=datetime.now) # дата создания проекта, тип DateTime, должно добавляться автоматически в момент создания проекта.
    close_date = Column(DateTime, default=None, nullable=True) # дата закрытия проекта, DateTime, проставляется автоматически в момент набора нужной суммы.
