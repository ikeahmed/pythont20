import requests

response = requests.get('http://api.twitter.com/?apikey=6d2c6568&y=2019')
print (response) 
print (response.status_code)
print (response.text)

#Open a terminal window and run "pip install requests" command, to download & install requests module from internet

#following are some attributes of response object
#response.status_code
#response.text


#replace url with any of the following and see the response object in debug mode
#http://ron-swanson-quotes.herokuapp.com/v2/quotes
#http://www.omdbapi.com
#http://www.omdbapi.com/?apikey=6d2c6568&t=superman #search movie by title superman
#http://www.omdbapi.com/?apikey=6d2c6568&t=black+panther  #search movie by title black panther 
#http://www.omdbapi.com/?apikey=6d2c6568&i=tt1825683 # search black panther movie by iMDB id
#http://www.omdbapi.com/?apikey=6d2c6568&y=2019 #search all movies in 2019, gives error
#http://api.twitter.com/?apikey=6d2c6568&y=2019 #calling twitter api, gives error but compare this error with above
#http://www.httpbin.org/get
#https://automatetheboringstuff.com/files/rj.txt # will download romeo and juliet drama
#https://gturnquist-quoters.cfapps.io/api/random # random quote about java spring boot technology 
#http://httpbin.org/get #simple http request and response service . good for testing get, post, put and delete
#https://api.exchangeratesapi.io/latest 
#url = 