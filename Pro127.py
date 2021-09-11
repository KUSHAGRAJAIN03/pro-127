import requests as r
from bs4 import BeautifulSoup
import csv
import pandas as pd

Url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = r.get(Url)

soup = BeautifulSoup(page.content,"html.parser")
data  = []

Div = soup.find("table")
row_list = []
table_rows = Div.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    row_list.append(row)

header = ["Name","Distance","Mass","Radius"]

with open ("project1.csv","a+",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(row_list)
    
