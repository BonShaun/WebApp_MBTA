import urllib.request
import json
from pprint import pprint




MAPQUEST_API_KEY = 'kmg2FmXvTcYVSTWKkTRlx2AoMlcBFiUT'
location = Babson
url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
# pprint(response_data)
print(response_data["results"][0]["locations"][0]['postalCode'])
latLng_dict = response_data["results"][0]["locations"][0]['latLng']
print("Babson's Latitude is:", latLng_dict["lat"], "and Longitude is:", latLng_dict["lng"])
# 02481

# MAPQUEST_API_KEY = 'e226d8e1dae2416d912aafa8a96a6bec'
# location = input("Location: ")
# url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location}'
# f = urllib.request.urlopen(url)
# response_text = f.read().decode('utf-8')
# response_data = json.loads(response_text)
