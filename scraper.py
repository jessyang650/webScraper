from bs4 import BeautifulSoup
import requests

source = requests.get('https://woodworkingformeremortals.com/plans/').text

soup = BeautifulSoup(source, 'lxml')

for columns in soup.find_all('ul'):
    project = columns.li.a.text
    pdf_links = columns.li.a
    print(project)
    print(pdf_links.get('href'))