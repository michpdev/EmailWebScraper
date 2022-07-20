#Web scraper to pull text from Cornell Class website 
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://classes.cornell.edu/browse/roster/FA22/subject/AAS"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.title)

professors = []

class_list = soup.findAll('span', attrs={"class":"tooltip-iws", "data-toggle":"popover"})
for prof in class_list:
	if "(" in prof['data-content'] and "Letter" not in prof['data-content']:
		t = prof['data-content'].split()
		professor = {}
		professor['first'] = t[0]
		professor['last'] = t[1]
		professor['netid'] = t[2].replace("(","").replace(")","")
		professor['email'] = professor['netid']+"@cornell.edu"
		professors.append(professor)

filename = 'professors.csv'

with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['first','last','netid','email'])
	w.writeheader()
	for profes in professors:
		w.writerow(profes)		

'''
professors=[] # a list to store professors

table = soup.find('div', attrs = {"data-roster-slug":"FA22"})

for row in table.findAll('span',
						attrs = {'class':'tooltips-iws'}):
	professor = {}
	professor['first'] = row.text['data-content']
	professor['last'] = row.a['href']
	professor['netid'] = row.img['src']
	professors.append(professor)

filename = 'professors.csv'
with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['first','last','netid'])
	w.writeheader()
	for professor in professors:
		w.writerow(professor)
'''


