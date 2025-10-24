#to run this script, paste 'python3 scraper-python.py' in your terminal

import requests
from bs4 import BeautifulSoup
import re

def scrape():

    url = 'https://pds-atmospheres.nmsu.edu/data_and_services/atmospheres_data/PERSEVERANCE/logs/MARS22_MEDA_WS_CAlibrated_Del13.htm'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    text = soup.get_text()

    matches = re.findall(r'urn.*?_____p', text)

    for m in matches:
        print(m)
    
    
if __name__ == '__main__':
    scrape()