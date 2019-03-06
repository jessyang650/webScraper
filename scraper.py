from bs4 import BeautifulSoup
import requests
import csv

html = requests.get('https://woodworkingformeremortals.com/plans/').text

soup = BeautifulSoup(html, 'lxml')

csv_file = open('wood_working_plans.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['PROJECTS', 'PLANS'])

for columns in soup.find_all('ul')[2:-1:]:
    projects = columns.li.a.text
    plans = columns.li.a.get('href')

    print(projects)
    print(plans)

    csv_writer.writerow([projects, plans])

csv_file.close()