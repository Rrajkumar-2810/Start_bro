#Python Requests: is a python library used to get requests from the web server.
#Reasons for using: Do not have to manually add query strings to URL's, or form-encode Post data.
#Get requests: Is used to request the data from the server.
#Post requests: Is used to submit the data to be processed to the server.

import requests
payload = {'key1' : 'value1', 'key2' : 'value2'}
cookies = dict(key1 = 'value1', key2 = 'value2') #Cookies and Headers
res = requests.get('https://httpbin.org/get', params=payload)
pos = requests.post('https://httpbin.org/post', params=payload)
co = requests.get('https://httpbin.org/cookies', cookies=cookies)

'''
print(res.url)
print()
print(res.text)
print(res.status_code)
print(res.headers)
print(res.json())
print(res.cookies)
'''

'''
print(pos.url)
print()
print(pos.text)
'''

#print(co.text)

