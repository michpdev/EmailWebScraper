#Web scraper to pull text from Cornell Class website 
import requests
from bs4 import BeautifulSoup
import csv


URL = "https://classes.cornell.edu/browse/roster/FA22/subject/AMST"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.title)

professors = []


class_list = soup.findAll('span', attrs={"class":"tooltip-iws", "data-toggle":"popover"})
for prof in class_list:
	if "(" in prof['data-content'] and "Letter" not in prof['data-content'] and "Satisfactory" not in prof['data-content']:
		t = prof['data-content'].split()
		professor = {}
		professor['first'] = t[0]
		if (t[2][0].isupper()): 
			professor['last'] = t[1]+" "+t[2]
			professor['netid'] = t[3].replace("(","").replace(")","")
		else:
			professor['last'] = t[1]
			professor['netid'] = t[2].replace("(","").replace(")","")
		
		professor['email'] = professor['netid']+"@cornell.edu"
		professors.append(professor)


no_dup = []
for i in professors:
    if i not in no_dup:
        no_dup.append(i)
filename = 'professors.csv'

with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['first','last','netid','email'])
	w.writeheader()
	for profes in no_dup:
		w.writerow(profes)		

