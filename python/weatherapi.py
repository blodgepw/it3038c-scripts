import json 
import requests


print('Please enter your zip code: ')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s&appid=fd12a98450535ccc428e00c2b4e51c21' % zip)

data = r.json()

print(data['weather'][0]['description'])

#dictionaries are in { } and use key value pairs
#lists are in [ ] and use numeric indexes [0-n]