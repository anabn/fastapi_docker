# patient-service/app/api
from app.api.models import PatientInputData, PatientOutputData, PatientUpdateData
from app.api.db import patient, database


async def add_patient(payload: PatientInputData):
    query = patient.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_patient():
    query = patient.select()
    return await database.fetch_all(query=query)

async def get_patient(id):
    query = patient.select(patient.c.id==id)
    return await database.fetch_one(query=query)

async def delete_patient(id: int):
    query = patient.delete().where(patient.c.id==id)
    return await database.execute(query=query)

async def update_patient(id: int, payload: PatientInputData):
    query = (
        patient
        .update()
        .where(patient.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)