# Initial code from video @ https://www.youtube.com/watch?v=GBQAKldqgZs
import requests

r = requests.get('https://api.github.com/user', auth=('user','pass'))
print(r.status_code)

r.headers['content-type']
