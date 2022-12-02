

from requests_html import HTMLSession
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date

class_name = 'container__headline __headline'
keyword = 'covid'
url_base = 'https://edition.cnn.com/search?q=' + keyword + '&from=0&size=10&page=1&sort=newest&types=all&section='

res = requests.get(url_base)
soup = BeautifulSoup(res.content, 'html.parser')
headlines = soup.find_all('span',{'data-editable','headline'})

print(headlines)
