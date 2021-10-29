import json
import requests

url="https://api.data.gov.sg/v1/environment/24-hour-weather-forecast"
req=requests.get(url)

data = json.loads(req.text)

# print update timestamp
update_time = data["items"][0]["update_timestamp"]
print("Update time: " + update_time)

# print forecast
forecast = data["items"][0]["general"]["forecast"]
print("Forecast: " + forecast)


'''
helloFile = open("weather.txt", "a")
helloFile.write("Weather is " + forecast + "\n\n")
helloFile.close()

'''

periods = data["items"][0]["periods"]

# printing all values
print("----------------- Print Info for different regions ------------------")
for period in periods:
    start = period["time"]["start"]
    #weather = forecast["forecast"]
    west_region = period["regions"]["west"]
    east_region = period["regions"]["east"]
    central_region = period["regions"]["central"]
    south_region = period["regions"]["south"]
    north_region = period["regions"]["north"]
            
    print(start)
    print("West Region: " + west_region)
    print("East Region: " + east_region)
    print("Central Region: " + central_region)
    print("South Region: " + south_region)
    print("North Region: " + north_region)
    
    print()