# aprs_beacon.py

import time
import sys
import json
import aprslib
import datetime
from datetime import datetime
import pip._vendor.requests
from pip._vendor import requests

# load properties
def load_properties(filepath):
    props={}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("!"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                props[key.strip()] = value.strip()
    return props

props = load_properties("aprs_beacon.properties")

print(props)

wundergroundStationId = props["wundergroundStationId"]
wundergroundApiKey = props["wundergroundApiKey"]
aprsCallsign = props["aprsCallsign"]
aprsPasscode = props["aprsPasscode"]


# get weather data from Wunderground as json
url = "https://api.weather.com/v2/pws/observations/current?stationId="+wundergroundStationId+"&format=json&units=e&apiKey="+wundergroundApiKey
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    print(data)
else:
    print(f"Error retrieving data, status code: {response.status_code}")

# get date from request
temperature = data['observations'][0]['imperial']['temp']
humidity = data['observations'][0]['humidity']
pressure = data['observations'][0]['imperial']['pressure']
wind_direction = data['observations'][0]['winddir']
wind_speed = data['observations'][0]['imperial']['windSpeed']
wind_gust = data['observations'][0]['imperial']['windGust']
rainfall_since_midnight = data['observations'][0]['imperial']['precipTotal']
percipRate = data['observations'][0]['imperial']['precipRate']
lon = data['observations'][0]['lon']
lat = data['observations'][0]['lat']

print("temperature", temperature)
print("humidity", humidity)
print("pressure", pressure)
print("wind_direction", wind_direction)
print("wind_speed", wind_speed)
print("wind_gust", wind_gust)
print("rain_since_midnight", rainfall_since_midnight)
print("percipRate", percipRate)
print("lon", lon)
print("lat", lat)

# converting pressure from inHg to mbar
def inhg_to_mbar(inhg_value:float) -> float:
    return inhg_value * 33.8638866667
pressure = (inhg_to_mbar(pressure) + 20) * 10

#converting rain values 1/100 inch
rainfall_since_midnight = rainfall_since_midnight * 100
percipRate = percipRate * 100

# formatting weather data
temperaturestr = str("%03d" % temperature)
humiditystr = str ("%02d" % humidity)
pressurestr = str ("%05d" % pressure)
wind_directionstr = str ("%03d" % wind_direction)
wind_speedstr = str ("%03d" % wind_speed)
wind_guststr = str ("%03d" % wind_gust)
rainfall_since_midnightstr = str ("%03d" % rainfall_since_midnight)
percipratestr = str ("%03d" % percipRate)

print("temperaturestr", temperaturestr)
print("humiditystr", humiditystr)
print("pressurestr", pressurestr)
print("wind_directionstr", wind_directionstr)
print("wind_speedstr", wind_speedstr)
print("wind_guststr", wind_guststr)
print("rainfall_since_midnightstr", rainfall_since_midnightstr)
print("percipRate", percipRate)

# convert time to UTC
UTC = datetime.utcnow()
formatted_utc = UTC.strftime('%H%M%S')
print("formatted_utc", formatted_utc)

# my fixed coords for now, could be converted from wunderground lon/lat data
coords = "5041.35N/00710.98E"

# combine APRS payload
APRS_String  = aprsCallsign+">APRS,TCPIP*:@"+formatted_utc+"z"+coords+"_"+wind_directionstr+"/"+wind_speedstr+"g"+wind_guststr+"t"+temperaturestr+"r"+percipratestr+"P"+rainfall_since_midnightstr+"h"+humiditystr+"b"+pressurestr+"powered by wunderground.com"

# send via TCPIP on port 14580 with appropriate passcode
#AIS = aprslib.IS(aprsCallsign, aprsPasscode, port=14580)
#AIS.connect()
#AIS.sendall(APRS_String)

print(APRS_String)
