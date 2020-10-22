# patient-service/app/api

from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import PatientInputData, PatientOutputData, PatientUpdateData
from app.api import db_manager
from app.api.service import is_drug_present

patient = APIRouter()

#   POST 
@patient.post('/', response_model=PatientOutputData, status_code=201)
async def create_patient(payload: PatientInputData):
    for drug_id in payload.drugs_id:
        if not is_drug_present(drug_id):
            raise HTTPException(status_code=404, detail=f"Prescriptions id:{drug_id} drugs not found")
    patient_id = await db_manager.add_patient(payload)
    response = {
        'id': patient_id,
        **payload.dict()
    }
    return response


#   GET ALL 
@patient.get('/', response_model=List[PatientOutputData])
async def get_all_patients():
    get_all_patient = await db_manager.get_all_patient()
    return get_all_patient

#   GET BY ID
@patient.get('/{id}/', response_model=PatientOutputData)
async def get_patient(id: int):
    patient = await db_manager.get_patient(id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found in this db")
    return patient

#   PUT / UPDATE
@patient.put('/{id}/', response_model=PatientOutputData)
async def update_patient(id: int, payload: PatientUpdateData):
    patient = await db_manager.get_patient(id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found in this db")
    update_data = payload.dict(exclude_unset=True)

    if 'drugs_id' in update_data:
        for drug_id in payload.drugs_id:
            if not is_drug_present(drug_id):
                raise HTTPException(status_code=404, detail=f"Prescriptions id:{drug_id} drugs not found")

    patient_in_db = PatientInputData(**patient)

    updated_patient = patient_in_db.copy(update=update_data)

    return await db_manager.update_patient(id, updated_patient)

#   DELETE
@patient.delete('/{id}/', response_model=None)
async def delete_patient(id: int):
    patient = await db_manager.get_patient(id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found in this db")
    return await db_manager.delete_patient(id)