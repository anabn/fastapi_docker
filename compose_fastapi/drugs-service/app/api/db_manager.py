# drugs-service/app/api
from app.api.models import DrugsInput, DrugsOutput, DrugsUpdate
from app.api.db import drugs, database


async def add_drug(payload: DrugsInput):
    query = drugs.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_drug(id):
    query = drugs.select(drugs.c.id==id)
    return await database.fetch_one(query=query)