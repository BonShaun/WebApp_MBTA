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

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data



def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    place_name = place_name.replace(' ','%20')
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    response_data = get_json(url)
    pprint(response_data)
    response_latlng = response_data['results'][0]['locations'][0]['displayLatLng']
    # pprrint(response_latlng)
    lat = response_latlng['lat']
    lng = response_latlng['lng']
    return lat,lng

# print(get_lat_long("Prudential Center"))





def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url_MBTA = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    response_data_MBTA = get_json(url_MBTA)

    try:
        station = response_data_MBTA['data'][0]['attributes']['name']
        wheelchair = response_data_MBTA['data'][0]['attributes']['wheelchair_boarding']
        return station, wheelchair
    except:
        return None, None

# print(get_nearest_station(42.3489, -71.08182))

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat, lng = get_lat_long(place_name)
    stop, station_accessible = get_nearest_station(lat,lng)
    if station_accessible == 1:
        station_accessible = "Accessible"
        
    elif station_accessible == 2:
        station_accessible = "Inaccessible"
        
    else:
        station_accessible = "Accessibility data unavailable"
        
    return stop, station_accessible

        #return should be simple as possible. dont return full sentence. Just return "Station Name. True"


# <<<<<<< HEAD
# <<<<<<< HEAD
# def main():
#     """
#     You can all the functions here
#     """
#     print(find_stop_near('Prudential Center'))
# =======
# =======
# >>>>>>> ac0c2036543f4af44530725d59c237d1431e2d55
# def main():
#     """
#     You can all the functions here
#     """
#     print(find_stop_near('Babson College'))
# <<<<<<< HEAD
# >>>>>>> ac0c2036543f4af44530725d59c237d1431e2d55
# =======
# >>>>>>> ac0c2036543f4af44530725d59c237d1431e2d55


# if __name__ == '__main__':
#     main()
#     # pass
