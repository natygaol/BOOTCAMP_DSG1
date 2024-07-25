import requests
from prefect import task
from config import Config

config = Config()

@task(name="Extrar info de dni")
def task_extract_dni(dni):
    data_request = {
        "dni": dni 
    }

    headers_request = {
        "Authorization": "Bearer " + config.api_token,
        "Content-Type": "application/json"
    }
    response = requests.post(config.api_url_dni,
                             json=data_request,
                             headers=headers_request)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"error {response.status_code}")