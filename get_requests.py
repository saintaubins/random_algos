import requests


#################################################################
#############      These are the get requests       #############

#url = 'https://developer.veevavault.com/api/20.3/app/cdm'
# username = ''
# password = ''
#payload = {'firstName': 'John', 'lastName': 'Smith'}
#url2 = 'https://httpbin.org/get'
#url1 = 'https://developer.veevavault.com/api/20.3/query'
#headers_dict = {'Authorization': {SESSION_ID}}
#headers = {'Content-Type':'application/x-www-form-urlencoded','username': username}
#response = requests.get(url1, params=payload  )
#print(response.headers)
#print(response.headers['content-type'])

# print(dir(response)) will show all attributes and methods available
# print(help(response)) will show a more detailed definition of the methods
#print(dir(response))

'''
print(response.url)
print(response.status_code)
print(response.content) # not recommented as not really formatted to a json view.
print(response.text)

print(response.json)
'''

#################################################################
############     these are the post requests    #################

'''
url3 = 'https://httpbin.org/post'

response = requests.post(url3, data=payload  ) # data key word does a conversion from a form as by default it is expecting a form.

print(response.text)
print(response.url)
response_dict = response.json()
print(response_dict['form'])
'''


#################################################################
###############        Login starts here        #################


r = requests.get('https://httpbin.org/basic-auth/sem/testing', auth=('sem','testing'), timeout=3)

print(r.text)



