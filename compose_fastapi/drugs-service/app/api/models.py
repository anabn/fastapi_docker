# drugs-service/app/api
from pydantic import BaseModel
from typing import List, Optional

class DrugsInput(BaseModel):
    name: str
    designation: Optional[str] = None


class DrugsOutput(DrugsInput):
    id: int


class DrugsUpdate(DrugsInput):
    name: Optional[str] = None