import os
import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.ibm.com').text

soup = BeautifulSoup(r, 'html5lib')

print(soup.prettify())

path = os.path.join(os.getcwd(), 'ibm.html')
with open(path, 'w', 'utf-8') as f:
    f.write(soup.prettify())
