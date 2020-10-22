# patient-service/app/api
import os
import httpx

DRUGS_SERVICE_HOST_URL = 'http://192.168.16.6:8080/api/v1/drugs/'

def is_drug_present(drug_id: int):
    url = os.environ.get('DRUG_SERVICE_HOST_URL') or DRUGS_SERVICE_HOST_URL
    url = DRUG_SERVICE_HOST_URL
    r = httpx.get(f'{url}{drug_id}/')
    return True if r.status_code == 200 else False