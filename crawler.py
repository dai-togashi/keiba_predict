import requests
from bs4 import BeautifulSoup

def url_to_soup(url):
    req = requests.get(url)
    return BeautifulSoup(req.content, 'html.parser')

soup = url_to_soup('https://www.platform-one.co.jp/contact/index.php?act=input')
print(soup.prettify())