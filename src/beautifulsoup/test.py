import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date
today = date.today()
d = today.strftime("%m-%d-%y")
print("date =" ,d)

nbc_business = "https://www.nbcnews.com/business"
res = requests.get(nbc_business)
soup = BeautifulSoup(res.content, 'html.parser')
headlines = soup.find_all('span',{'class','tease-card__headline'})

for i in headlines:
    print(i.text)