import requests
from bs4 import BeautifulSoup

HOME_URL = 'https://www.nankankeiba.com'

def url_to_soup(url):
    req = requests.get(url)
    return BeautifulSoup(req.content, 'html.parser')

def horse_page_link(url):
    soup = url_to_soup(url)
    link_list = [HOME_URL + x.get('href') for x in soup.find_all('a', class_='tx-mid tx-low') ]
    return link_list

#soup = url_to_soup('https://www.platform-one.co.jp/contact/index.php?act=input')
#print(soup.prettify())

horse_page_link_list = horse_page_link('https://www.nankankeiba.com/race_info/2018071921050110.do')
print(horse_page_link_list)