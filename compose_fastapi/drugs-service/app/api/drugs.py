# drugs-service/app/api
from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import DrugsInput, DrugsOutput, DrugsUpdate
from app.api import db_manager

drugs = APIRouter()

@drugs.post('/', response_model=DrugsOutput, status_code=201)
async def create_drug(payload: DrugsInput):
    drug_id = await db_manager.add_drug(payload)

    response = {
        'id': drug_id,
        **payload.dict()
    }
    
    return response

@drugs.get('/{id}/', response_model=DrugsOutput)
async def get_drug(id: int):
    drug = await db_manager.get_drug(id)
    if not drug:
        raise HTTPException(status_code=404, detail="Drug not found")
    return drug