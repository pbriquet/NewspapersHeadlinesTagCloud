import requests
import json


def main(url):
    with requests.Session() as req:
        for item in range(1, 1000, 100):
            r = req.get(url.format(item)).json()
            for a in r['result']:
                print("Headline: {}, Url: {}".format(
                    a['headline'], a['url']))


main("https://search.api.cnn.io/content?q=coronavirus&sort=newest&category=business,us,politics,world,opinion,health&size=100&from={}")