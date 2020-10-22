# patient-service/app
from fastapi import FastAPI
from app.api.patient import patient
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/patients/openapi.json", docs_url="/api/v1/patients/docs")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(patient, prefix='/api/v1/patients', tags=['patients'])