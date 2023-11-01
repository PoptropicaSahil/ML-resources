# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
#pos = input('start at position - ')
#times = input('how many times - ')
lst = list()
tags = soup('a')
for tag in tags:
    #for step in range(4) :
    y = (tag.get('href', None))
    print(y)
    #print(type(y))
    lst.append(y)
print(lst[2])               #gives the 3rd term first times

url = lst[2]
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
lst = list()

print('.......................')
tags = soup('a')
for tag in tags:
    #for step in range(4) :
    y = (tag.get('href', None))
    print(y)
    #print(type(y))
    lst.append(y)

print(lst[2])



#print(start)
