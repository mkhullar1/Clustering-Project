import numpy
import datetime
startDate = datetime.datetime(2010, 1, 1)
endDate = datetime.datetime(2019, 5, 1)

import pandas_datareader as pdr
stock = pdr.get_data_yahoo("AMZN", startDate, endDate)

print(stock)

import pandas as pd

print(stock["Adj Close"])

from lxml import html
import requests

page = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
tree = html.fromstring(page.content)
table = tree.xpath('//*[@id="mw-content-text"]/div/table[1]')
print(table)
table = table[0]
print(table)

rows = table.findall("tr")
print(rows)

for x in rows:
    firstCell = x.find("td")
    if firstCell!=None:
        print(firstCell.text_content())

stocksArray = []
for x in rows:
    firstCell = x.find("td")
    if firstCell!=None:
        stocksArray.append(firstCell.text_content())
print(stocksArray)

import csv
with open("stocksArray.csv", "wt") as f:
    writer = csv.writer(f)
    writer.writerow(stocksArray)

import pandas as pd
table = tree.xpath('//*[@id="mw-content-text"]/div/table[1]')
table = table[0]
rows = table.findall("tr")
rows = rows[1:]
cellsAr = []
for x in rows:
    cells = x.findall("td")
    cells = [x.text_content() for x in cells]
    cellsAr.append(cells)
df = pd.DataFrame(cellsAr)
df.columns = ["Ticker","Security","SEC Filings","GICS Sector","GICS Sub Industry","Address","Date Added","CIK"]
df.to_csv("SP500.csv",encoding="UTF-8")



import pandas as pd
import statsmodels.formula.api as sm
df = pd.DataFrame.from_csv("StockData.csv", encoding="UTF-8")
model = sm.ols(formula="PXD ~ Index + Oil + Gold + NaturalGas", data=df)