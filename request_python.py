from time import time
import requests
from bs4 import BeautifulSoup

r = requests.get('https://xkcd.com/353/')

# print(r)
# print(dir(r))
# print(help(r))
# print(r.text)

""" soup = BeautifulSoup(r.text, 'lxml')

# get the image
image_src = soup.find('div', id='comic').img['src']
image_url = 'https:' + image_src
image_name = image_url.split('/')[-1]

# download the image
r = requests.get(image_url)
with open('comic.png', 'wb') as f:
    f.write(r.content) """

""" print(r.status_code)
print(r.ok)
print(r.headers) """

""" payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)

print(r.text)
print(r.url) """

""" payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)

# print(r.text)
# print(r.url)
r_dict = r.json()
print(r_dict['form']) """
""" 
r = requests.get('https://httpbin.org/basic-auth/corey/testing',auth=('corey','testing'))

print(r.text)
 """

""" 
r = requests.get('https://httpbin.org/basic-auth/corey/testing',auth=('corey','testin'))

print(r)
"""

""" 
r = requests.get('https://httpbin.org/delay/1',timeout=3)
print(r)
r = requests.get('https://httpbin.org/delay/6',timeout=3)
print(r) 
"""
