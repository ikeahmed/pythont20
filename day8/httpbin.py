import requests
r = requests.get('https://httpbin.org/get')
print (r.text)

payload = {"firstName": "Ikhlas","lastName":"Ahmed"}
r= requests.get('https://httpbin.org/get',params=payload)
print(r.text)