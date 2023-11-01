import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving.....', url)
    uh = urllib.request.urlopen(address, context=ctx)       #yaha par bhi change kiya hai, sirf address(input) daala hai, wo jo url upar convert karke bant hai, wo kuch bhala hi ho jata hai!!
    #op!!

    sum = 0
    data = uh.read()
    #print('Retrieved....', len(data), 'characters')
    #print(data.decode())
    #print(data)
    tree = ET.fromstring(data)
    lst = tree.findall('comments/comment')      #comments/comment is exactly similar to users/user
    #print(data)
    #counts = tree.findall('.//comment')        #ye kuch kaam nahi aaya, isne shayad address diya hai
    for item in lst :
        print('name is ',item.find('name').text)
        print('count is ',item.find('count').text)
        y = item.find('count').text
        #print('y is',y)
        sum = sum + int(y)
    #print(counts)
    break

print(sum)
