import requests
import os

token = os.getenv('APIPERU_TOKEN')
url_tipo_de_cambio = ' https://apiperu.dev/api/tipo_de_cambio'

fecha = input("ingrese fecha: ")
moneda = input("ingrese moneda(USD): ")

data_request = {
    "fecha": fecha,
    "moneda": moneda
}

headers_request = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}

response = requests.post(url_tipo_de_cambio,json=data_request,headers=headers_request)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error {response.status_code}")