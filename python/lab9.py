import json 
import requests

r = requests.get('http://localhost:3000')

data = r.json()

print(data[0]['name'] + ' is ' + data[0]['color'])
print(data[1]['name'] + ' is ' + data[1]['color'])
print(data[2]['name'] + ' is ' + data[2]['color'])
print(data[3]['name'] + ' is ' + data[3]['color'])

#Widget1 is blue.
#Widget2 is green.
# Widget whatever is whatever...


#dictionaries are in { } and use key value pairs
#lists are in [ ] and use numeric indexes [0-n]