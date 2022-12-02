from requests_html import HTMLSession


keyword = 'covid'
url_base = 'https://news.google.com/rss/search?q='

url = url_base + keyword

s = HTMLSession()

r = s.get(url)

for title in r.html.find('title'):
    print(title.text)