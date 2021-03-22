import requests, re
from bs4 import BeautifulSoup

r = requests.get('https://www.courts4sports.com').content

soup = BeautifulSoup(r, "lxml")

for link in soup.find_all('a', attrs={'href':re.compile("^https://www.courts4sports.com/cva/")} ):
    print(link.get('href'))
