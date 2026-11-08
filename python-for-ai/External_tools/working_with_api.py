
import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

data['current']['temperature_2m']


import requests

def get_weather(Latitude,Longitude):
    url=f"https://api.open-meteo.com/v1/forecast?latitude={Latitude}&longitude={Longitude}&current=temperature_2m"
    response=requests.get(url)
    data=response.json()
    return data['current']['temperature_2m']

paris_temperature=get_weather(48.85,2.35)
islamabad_temperature=get_weather(33.6844,73.0479)
print(f"Temperature in Paris: {paris_temperature}°C")
print(f"Temperature in Islamabad: {islamabad_temperature}°C")

import requests

url = "https://restcountries.com/v3.1/name/pakistan"
response = requests.get(url)
data = response.json()   # list ka pehla item

print(data)      # ['Islamabad']