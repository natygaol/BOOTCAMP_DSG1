import requests
from bs4 import BeautifulSoup

url = "https://www.bcrp.gob.pe/"

def obtener_tipocambio(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = BeautifulSoup(response.text, 'html.parser')
        table = html.find('table', {'class': 'tip-table'})
        
        if table:
            tds = table.find_all('td')
            for td in tds:
                print(td.get_text())
        else:
            print("No se encontró la tabla con la clase 'tip-table'.")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    obtener_tipocambio(url)
