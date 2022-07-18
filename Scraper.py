#Web scraper to pull text from Cornell Class website 
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://classes.cornell.edu/browse/roster/FA22/subject/CS"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

professors=[] # a list to store professors

table = soup.find('div', attrs = {"data-roster-slug":"FA22"})

for row in table.findAll('span',
						attrs = {'class':'tooltips-iws'}):
	professor = {}
	professor['first'] = row.h5.text
	professor['last'] = row.a['href']
	professor['netid'] = row.img['src']
	professors.append(professor)

filename = 'professors.csv'
with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['first','last','netid'])
	w.writeheader()
	for professor in professors:
		w.writerow(professor)
