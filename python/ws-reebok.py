import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.xbox.com/en-US/games/microsoft-flight-simulator").content

soup = BeautifulSoup(data, 'html.parser')
d = soup.findAll("div", {"class":"module-accentuated-price c-heading-2 x-p-t-0x"})
print(d) 