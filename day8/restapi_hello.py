import requests

response = requests.get('http://api.twitter.com/?apikey=6d2c6568&y=2019')
print (response) 
print (response.status_code)
print (response.text)

