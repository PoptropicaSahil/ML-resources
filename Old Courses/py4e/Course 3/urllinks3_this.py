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
pos = int(input('start at position - '))
times = int(input('how many times - '))

for count in range(times) :

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')           #yeh to normal hai
    lst = list()
    tags = soup('a')
    for tag in tags:
        y = (tag.get('href', None))
        ##print(y)
        #print(type(y))                     STRING MILTI HAI
        lst.append(y)
    print(lst[pos-1])                          #DIYA HAI STARTS WITH 1
    url = lst[pos-1]                            #BECOMES NEW URL
