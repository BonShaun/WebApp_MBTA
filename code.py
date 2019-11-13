import urllib.request
import urllib.parse
import json
from pprint import pprint

MAPQUEST_API_KEY = 'Ing5xxWtWc0FrjDV2W0vA7EVMFtiIj7N'
MBTA_API_KEY = '6018a853c6e8432694c83919c91e0892'
MAPQUEST_BASE_URL = "http://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


def ask_location(loc):
    d = {}
    d['location'] = loc
    variable = urllib.parse.urlencode(d)
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&{variable}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    latlng = (response_data['results'][0]['locations'][0]['displayLatLng'])
    return latlng

latlng = ask_location('Prudential Center')
print(latlng)
lat = latlng['lat']
lng = latlng['lng']
index = 0



url_MBTA = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={lat}&filter[longitude]={lng}&sort=distance'
f_MBTA = urllib.request.urlopen(url_MBTA)
response_text_MBTA = f_MBTA.read().decode('utf-8')
response_data_MBTA = json.loads(response_text_MBTA)
station = response_data_MBTA['data'][0]['attributes']['name']
wheelchair = response_data_MBTA['data'][0]['attributes']['wheelchair_boarding']






