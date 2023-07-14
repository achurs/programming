import requests
import json

key = "33feeee801e54c3a64dd577038e7cbce"
weather_api = "http://api.openweathermap.org/data/2.5/weather"

ip_location_url = "http://ip-api.com/json/"
ip_response = requests.get(ip_location_url).json()
print("The Response was ", ip_response['status'])
print('your location is', ip_response['city'])
lat = ip_response['lat']
lon = ip_response['lon']

url = weather_api + "?lat=" + str(lat) + "&lon=" + str(lon) + "&APPID=" + key
response = requests.get(url)
data = response.json()

print('the weather is', data['weather'][0]['description'])
print('the temperature is', data['main']['temp'])
print('the humidity is', data['main']['humidity'])
print('the wind speed is', data['wind']['speed'])
print('the pressure is', data['main']['pressure'])
