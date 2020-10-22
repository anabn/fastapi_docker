#drugs-service/app
from fastapi import FastAPI
from app.api.drugs import drugs
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/drugs/openapi.json", docs_url="/api/v1/drugs/docs")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(drugs, prefix='/api/v1/drugs', tags=['drugs'])