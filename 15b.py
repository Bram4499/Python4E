#code by Bram Raatjes
#version: 2017/04/02

import urllib
import json

testplace = 'South Federal University'
realplace = 'University of Cambridge'

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = realplace

url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data))
except: js = None
if 'status' not in js or js['status'] != 'OK':
    print '==== Failure To Retrieve ===='
    print data
    

#print json.dumps(js, indent=4)

place_id = js["results"][0]["place_id"]
#lat = js["results"][0]["geometry"]["location"]["lat"]
#lng = js["results"][0]["geometry"]["location"]["lng"]
#print 'lat',lat,'lng',lng
location = js['results'][0]['formatted_address']
print location

print place_id