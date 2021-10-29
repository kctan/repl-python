# hdb carpark info
# https://data.gov.sg/dataset/hdb-carpark-information

import json
import requests

url="https://api.data.gov.sg/v1/transport/carpark-availability"
req=requests.get(url)

data = json.loads(req.text)

# print update timestamp
update_time = data["items"][0]["timestamp"]
print("Update time: " + update_time)

# carpark number
carpark_number = data["items"][0]["carpark_data"][0]["carpark_number"]
print("Carpark number: " + str(carpark_number))

# print forecast
#forecast = data["items"][0]["general"]["forecast"]
#print("Forecast: " + forecast)


'''
helloFile = open("weather.txt", "a")
helloFile.write("Weather is " + forecast + "\n\n")
helloFile.close()

'''

