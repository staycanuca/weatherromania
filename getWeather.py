"""
    This application scrapes the website http://vremea.ido.ro/****.htm
    in order to get the weather in ****.
    By default, it is set to get the weather from Mehedinti.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

county = "Mehedinti"

if(len(sys.argv) > 1):
    county = str(sys.argv[1])

print(len(sys.argv))
print(county)
page = requests.get("http://vremea.ido.ro/" + county + ".htm")

soup = BeautifulSoup(page.content, 'html.parser')

maxTemps = []
minTemps = []
dates = []

var = soup.find_all('tr', class_ = '2s dh')

for item in var:
    dates.append(item.find('b').get_text())
    maxTemps.append(item.find('small').get_text().split()[1])
    minTemps.append(item.find('small').get_text().split()[4])
    
weather = pd.DataFrame({"Date":dates, "Max Temps":maxTemps, "Min Temps":minTemps})