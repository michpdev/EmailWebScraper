# import library
from bs4 import BeautifulSoup
import requests
# Request to website and download HTML contents
url='https://classes.cornell.edu/browse/roster/FA22/subject/CS'
req=requests.get(url)
content=req.text

soup=BeautifulSoup(content)
