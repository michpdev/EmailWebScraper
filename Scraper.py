#Web scraper to pull text from Cornell Class website 
from time import sleep
import requests
from bs4 import BeautifulSoup
import csv

url_list = ["AAS","AEM","AEP","AGSCI", "AIIS", "ALS","AMST","ANSC",
"ANTHR","ARAB","ARCH","ARKEO","ART","ARTH","ASIAN","ASL","ASRC",
"ASTRO","BCS","BEE","BENGL","BIOAP","BIOEE","BIOG","BIOMG","BIOMI","BIOMS",
"BIONB","BME","BSOC","BTRY","BURM","CAPS","CEE","CHEM","CHEME","CHIN","CHLIT",
"CLASS","COGST","COML","COMM","CRP","CS","CZECH","DEA","DESIGN","DUTCH", "EAS",
"ECE","ECON","ENGL","ENGRC","ENTOM","ENVS","FDSC","FGSS","FINN",
"FREN","FSAD","GDEV","GERST","GOVT","GREEK","HADM", "HD",
"HEBRW","HIERO","HINDI","HIST","HUNGR","ILRHR","ILRLE","ILRLR",
"ILROB","ILRST","INDO","INFO","ITAL","JAPAN","JPLIT","JWST","KHMER",
"KOREA","LA","LATA","LATIN","LGBT","LING","MAE","MATH","MEDVL","MSE",
"MUSIC","NEPAL","NS","ORIE","PADM","PAM","PE","PERSN","PHIL","PHYS", 
"PLBIO","PLBRG","PLHRT","PLSCI","PLSCS","PMA","POLSH", "PORT","PSYCH",
"PUNJB","QUECH","RELST","ROMS","RUSSA","RUSSL","SANSK","SINHA", "SNLIT",
"SOC","SPAN","STS","STSCI","SWAHL","SWED","TAG","TAMIL","THAI","TIBET", "TURK",
"UKRAN","URDU","VIEN","VIET","VISST","WOLOF","WRIT","YORUB","ZULU"]
URL = "https://classes.cornell.edu/browse/roster/FA22/subject/"
professors = []


for x in url_list:
	r = requests.get(URL+x)
	soup = BeautifulSoup(r.content, 'html.parser')
	print(soup.title)
	sleep(2)
	class_list = soup.findAll('span', attrs={"class":"tooltip-iws", "data-toggle":"popover"})
	for prof in class_list:
		if "(" in prof['data-content'] and "Letter" not in prof['data-content'] and "Satisfactory" not in prof['data-content']:
			t = prof['data-content'].split()
			professor = {}
			professor['first'] = t[0]
			if (t[2][0].isupper() or t[2] =="van" or t[2] =="de"): 
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

