#Session objects: Session object persists certain parameters over multiple requests.
#Persists cookies across all requests made from the session instance
#Use urlib3 connection pooling which significantly increases performance
#A session object has all the methods of the main requests API
#Method level parameters override the session level parameters.

import requests

s= requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/456789123')
r = s.get('https://httpbin.org/cookies')
print(r.text)

#In the event of network connection, requests will raise a ConnectionError Exception.
#Response.raise_for_status() will raise an HTTP error when there is an unsuccesful status code.
#If there is a timeout, it will raise a timeout Exception.
#TooManyRedirects exception is raised if the requests exceeds the configured number of maximum number of redirections.
