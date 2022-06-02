#! python3
# Prints the weather for a location from the command line.

# 1. Reads the requested location from the command line
# 2. Downloads JSON weather data from OpenWeatherMap.org
# 3. Converts the string of JSON data to a Python data structure
# 4. Prints the weather for today and the next two days

# So the code will need to do the following:

# 1. Join strings in sys.argv to get the location.
# 2. Call requests.get() to download the weather data.
# 3. Call json.loads() to convert the JSON data to a Python data structure.
# 4. Print the weather forecast.

APPID = 'API_ID_HERE'

import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url ='https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
#print(response.text)

# Load JSON data into a Python variable
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']

print('Current weather is %s: ' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow: ')
print(w[1]['Weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow: ')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

# Ideas for Similar Programs
# Accessing weather data can form the basis for many types of programs. You
# can create similar programs to do the following:
# •	 Collect weather forecasts for several campsites or hiking trails to see which one will have the best weather.
# •	 Schedule a program to regularly check the weather and send you a frost alert if you need to move your plants indoors. (Chapter 17 covers scheduling, and Chapter 18 explains how to send email.)
# •	 Pull weather data from multiple sites to show all at once, or calculate and show the average of the multiple weather predictions.