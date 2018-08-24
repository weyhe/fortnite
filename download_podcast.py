import urllib.request

url = 'http://www.dr.dk/mu/Feed/ready-player-one-lydbog.xml?format=podcast&limit=500'

response = urllib.request.Request(url)

print(response)
