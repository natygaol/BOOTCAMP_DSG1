import requests
from prefect import task
from config import Config
import csv
import mysql.connector

config = Config()

@task(name='extraer info de csv')
def task_extract_csv(file_csv):
    with open(file_csv,mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        lista_csv = []
        for row in csv_reader:
            tupla_csv = (row['dni'],row['celular'])
            lista_csv.append(tupla_csv)

    return lista_csv

@task(name="Extraer info de dni")
def task_extract_dni(tupla_alumno):
    dni = tupla_alumno[0]
    celular = tupla_alumno[1]

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