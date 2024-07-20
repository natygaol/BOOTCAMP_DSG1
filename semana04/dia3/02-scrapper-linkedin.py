import requests
from bs4 import BeautifulSoup

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?geoId=102927786&keywords="

def get_offers(skill):
    url = requests.get(LINKEDIN_URL+skill)

    if(url.status_code == 200):
        html = BeautifulSoup(url.text,'html.parser')
        #print(html)
        offers = html.find('div',{'class':'base-search-card__info'})
        offers_title = html.find_all('h3',{'class':'base-search-card__title'})
        for title in offers_title:
            print(title.get_text())
    else:
        print(f"error : {url.status_code}")

if __name__ == '__main__':
    skill = input('ingrese skill a buscar : ')
    get_offers(skill)