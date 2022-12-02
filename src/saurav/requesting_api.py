import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

__loc__ = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
datapath = os.path.join(__loc__,'data')
sources_path = os.path.join(datapath,'sources.json')

def get_sources():
    r = requests.get('https://saurav.tech/NewsAPI/sources.json')
    sources =  r.json()

    # Writing to sample.json
    with open(os.path.join(datapath,'sources.json'), "w") as outfile:
        json.dump(sources, outfile)

def get_data():

    url_everything = 'https://saurav.tech/NewsAPI/everything/'
    with open(sources_path, 'r') as openfile:
        sources = json.load(openfile)['sources']

        for source in sources:
            url = url_everything + source['id'] + '.json'
            
            filepath = os.path.join(datapath,source['id'] + '.json')
            r = requests.get(url)
            print(str(r.ok) + ' ' + url)
            if(r.ok):
                data =  r.json()
                with open(filepath, "w") as outfile:
                    json.dump(data, outfile)


if __name__ == '__main__':
    get_data()