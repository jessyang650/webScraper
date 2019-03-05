from bs4 import BeautifulSoup
import requests

source = requests.get('https://woodworkingformeremortals.com/plans/').text

soup = BeautifulSoup(source, 'lxml')

for columns in soup.find_all('ul'):
    plans = columns.li.a
    print(plans)