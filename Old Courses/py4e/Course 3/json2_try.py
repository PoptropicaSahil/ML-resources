import urllib.request, urllib.parse, urllib.error
import json


api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'


while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    #url = serviceurl + urllib.parse.urlencode({'address': address})
    url = serviceurl
    print('Retrieving', url)

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    print('Retrieved', len(data), 'characters')
    print(data)
    ##data =

    try:
        js = json.loads(data)
    except:
        js = None

    print(json.dumps(js, indent=4))

    #info = json.loads(data)
    #print('User count:', len(info))

    #print(json.dumps(js, indent=4))

    #for item in info:
    #    print('Name', item['name'])
    #    print('Id', item['id'])
    #    print('Attribute', item['x'])

    break
