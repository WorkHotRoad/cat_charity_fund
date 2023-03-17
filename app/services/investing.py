from typing import List

from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Abstract


async def investing(
    obj_in: Abstract,
    model_db: Abstract,
    session: AsyncSession
) -> Abstract:
    source_db_all = await session.execute(
        select(model_db).where(
            model_db.fully_invested == 0
        ).order_by(model_db.create_date)
    )
    source_db_all = source_db_all.scalars().all()
    for source_db in source_db_all:
        obj_in, source_db = await invest(
            obj_in, source_db
        )
        session.add(obj_in)
        session.add(source_db)
    await session.commit()
    await session.refresh(obj_in)
    return obj_in


async def invest(
    obj_in: Abstract,
    obj_db: Abstract
) -> List[Abstract]:
    rem_obj_in = obj_in.full_amount - obj_in.invested_amount
    rem_obj_db = obj_db.full_amount - obj_db.invested_amount
    if rem_obj_in > rem_obj_db:
        obj_in.invested_amount += rem_obj_db
        obj_db = await close_donation(obj_db)
    elif rem_obj_in == rem_obj_db:
        obj_in = await close_donation(obj_in)
        obj_db = await close_donation(obj_db)
    else:
        obj_db.invested_amount += rem_obj_in
        obj_in = await close_donation(obj_in)
    return obj_in, obj_db


async def close_donation(
    obj_db: Abstract
) -> Abstract:
    obj_db.invested_amount = obj_db.full_amount
    obj_db.fully_invested = True
    obj_db.close_date = datetime.now()
    return obj_db
