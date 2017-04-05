import requests
from bs4 import BeautifulSoup

# set target url
site_url = ''

def collect(max_pages):
    page = 1
    while page < max_pages:
        url = site_url + str(page)
        html = requests.get(url)
        plain_text = html.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.select('h2 > a'):
            href = link.get('href')
            title = link.string
# print title
            print(title)
# print url
            print(href)            
#            print(soup.select('article div.entry-content')[0].get_text())
        
        page += 1

collect(10)
