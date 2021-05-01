import requests
import json

api1 = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=860863b0e5ae37e18466293074366188"
response = requests.request("GET", api1)
data = json.loads(response.content)
print(data)
print()
api2 = "https://api.nasa.gov/planetary/apod?api_key=YIDNrmCOAHqAMb2NpeubaaXMOV79dCMKTEn2p9Mb"
response2 = requests.request("GET", api2)
data2 = json.loads(response2.content)
print(data2)
