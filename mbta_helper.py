# Useful URLs (you need to add the appropriate parameters for your requests)
import urllib.request
import urllib.parse
import json
from pprint import pprint

MAPQUEST_API_KEY = 'Ing5xxWtWc0FrjDV2W0vA7EVMFtiIj7N'
MBTA_API_KEY = '6018a853c6e8432694c83919c91e0892'
MAPQUEST_BASE_URL = "http://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# Your API KEYS (you need to use your own keys - very long random characters)



# A little bit of scaffolding if you want to use it
def ask_location(place_name):
    d = {}
    d['location'] = place_name
    encoded_location = urllib.parse.urlencode(d)
    return encoded_location

    
variable = ask_location("Babson College")
url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&{variable}'

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

# print(get_json(url))

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    encoded_location = ask_location(place_name)
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&{encoded_location}'
    response_data = get_json(url)
    response_latlng = (response_data['results'][0]['locations'][0]['displayLatLng'])
    lat = response_latlng['lat']
    lng = response_latlng['lng']
    return (lat,lng)

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url_MBTA = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    f_MBTA = urllib.request.urlopen(url_MBTA)
    response_text_MBTA = f_MBTA.read().decode('utf-8')
    response_data_MBTA = json.loads(response_text_MBTA)

    try:
        station = response_data_MBTA['data'][0]['attributes']['name']
        wheelchair = response_data_MBTA['data'][0]['attributes']['wheelchair_boarding']
        return (station, wheelchair)
    except:
        return 'No stations are close enough'

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    latlng = get_lat_long(place_name)
    station_accessible = get_nearest_station(latlng[0],latlng[1])
    if station_accessible[1] == 1:
        return f'The closest station is {station_accessible[0]} and it is wheelchair accessible'
    elif station_accessible[1] == 2:
        return f'The closest station is {station_accessible[0]} and it is not wheelchair accessible'
    else:
        return f'The closest station is {station_accessible[0]} and there is no wheelchair accessibility data available'


def main():
    """
    You can all the functions here
    """
    print(find_stop_near('Prudential Center'))


if __name__ == '__main__':
    main()
