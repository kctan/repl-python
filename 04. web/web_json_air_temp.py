import json
import requests

url="https://api.data.gov.sg/v1/environment/air-temperature"
req=requests.get(url)

data = json.loads(req.text)

first_id = data["metadata"]["stations"][0]["id"]

# print the first item's id
print("id: " + first_id)

air_temp = data["items"][0]["readings"][0]["value"]

# print the first item's temperature 
print("air temp: " + str(air_temp))



stations = data["metadata"]["stations"]

print(len(stations))