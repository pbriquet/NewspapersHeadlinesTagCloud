import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import *
from newsapi import NewsApiClient

from wordcloud import WordCloud

newsapi = NewsApiClient(api_key='451de045f3bf4cc7a330311c5e191ac9')
sources = newsapi.get_sources()
sources_list = []
for source in sources['sources']:
    sources_list.append(source['id'])


n_days = 15
query = 'COVID'
page = 1
page_size = 100

def get_response_json(query, n_days, source, page_size, page):
    response_json = newsapi.get_everything(q=query,
        language='en',
        from_param=str(date.today() - timedelta(days=n_days)),
        to= str(date.today()),
        sources = source,
        page_size=page_size,
        page = page,
        sort_by='relevancy')
    return response_json

results = []

for i in range(50):
    results.append(get_response_json(query, n_days, sources_list[i], page_size, page))

print(len(results))
exit()

for i in range(len(results)):
    text_combined = ''
    for j in results[i]['articles']:
        text_combined += j['title'] + ''
    
    if text_combined is not '':
        wordcloud = WordCloud(max_font_size=40).generate(text_combined)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()