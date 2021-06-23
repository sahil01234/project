import requests
#import os
from datetime import datetime

api_key = 'e0526949d653b2554b8a22319cb5c095'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" +location+"&appid="+api_key+"&units=metric"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# create variables to store and display data
temp_city = ((api_data['main']['temp']))
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


# create file weather_output and append data
f = open('weather_output.txt', 'a')
f.write("-------------------------------------------------------------\n")
f.write("Weather Stats for - {}  || {} \n".format(location.upper(), date_time))
f.write("-------------------------------------------------------------\n")
f.write("Current temperature is: {:.2f} deg C \n".format(temp_city))
f.write("Current weather desc  :{} \n".format(weather_desc))
f.write("Current Humidity      :{} % \n".format(hmdt))
f.write("Current wind speed    :{} kmph \n".format(wind_spd))
f.close()

#print data
print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :", weather_desc)
print("Current Humidity      :", hmdt, '%')
print("Current wind speed    :", wind_spd, 'kmph')