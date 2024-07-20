import requests
from bs4 import BeautifulSoup
import mysql.connector

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?geoId=102927786&keywords="

def get_offers(skill):
    url = requests.get(LINKEDIN_URL+skill)

    if(url.status_code == 200):
        html = BeautifulSoup(url.text,'html.parser')
        #with open('linkedin.html','w',encoding='utf-8') as file:
        #    file.write(url.text)
        #print(html)

        ul_offers = html.find('ul',{'class':'jobs-search__results-list'})
        li_offers = ul_offers.find_all('li')
        
        for offer in li_offers:
            offer_title = offer.find('h3',{'class':'base-search-card__title'})
            offer_location = offer.find('span',{'class':'job-search-card__location'})
            offer_url = offer.find('a')['href'].strip()
            offer_company = offer.find('a',{'class':'hidden-nested-link'})
            company = offer_company.get_text().strip() if offer_company else 'N/A'

            print(f'titulo : {offer_title.get_text().strip()}')
            print(f'ubicacion : {offer_location.get_text().strip()}')
            print(f'empresa : {company}')
            print(f'url:{offer_url}')
    else:
        print(f"error : {url.status_code}")

if __name__ == '__main__':
    skill = input('ingrese skill a buscar : ')
    get_offers(skill)