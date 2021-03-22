import re
data = "Hello. My email is pblodgett2@gmail.com. Please contact me!"
p = re.compile('[A-z0-9_%.-]+@gmail\.com')
print(p.search(data).group())