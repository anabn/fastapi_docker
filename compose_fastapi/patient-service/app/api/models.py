# patient-service/app/api
from pydantic import BaseModel
from typing import List, Optional

# structure for data about patient

class PatientInputData(BaseModel):
    name: str
    surname: str
    age: int
    drugs_id: List[int]


class PatientOutputData(PatientInputData):
    id: int


class PatientUpdateData(PatientInputData):
    name: Optional[str] = None
    surname: Optional[str] = None
    age: Optional[int] = None
    drugs_id: Optional[List[int]] = None