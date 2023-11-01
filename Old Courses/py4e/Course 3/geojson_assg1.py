import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

#if api_key is False:
#    api_key = 42
#    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
#else :
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

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

    #url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(address, context=ctx)       #phir se yaha par address likha hai url ki jagah
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    #print('data is', data )

    try:
        js = json.loads(data)
    except:
        js = None

    #if not js or 'status' not in js or js['status'] != 'OK':
    #    print('==== Failure To Retrieve ====')
    #    print(data)
    #    continue

    print(json.dumps(js, indent=4))

    sum = 0

    for item in js['comments'] :
        #num = js['comments']
        count = item['count']
        print('count is' , count)
        sum = sum + count

    #lng = js['results'][0]['geometry']['location']['lng']
    #print('lat', lat, 'lng', lng)
    #location = js['results'][0]['formatted_address']
    #print(location)
    print('sum is' , sum)

    break
