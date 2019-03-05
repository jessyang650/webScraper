from bs4 import BeautifulSoup
import requests
import csv

html = requests.get('https://woodworkingformeremortals.com/plans/').text

soup = BeautifulSoup(html, 'lxml')

csv_file = open('wood_working_plans.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Project', 'Plans'])

for columns in soup.find_all('ul'):
    project = columns.li.a.text
    pdf_links = columns.li.a.get('href')

    print(project)
    print(pdf_links)

    csv_writer.writerow([project, pdf_links])

csv_file.close()