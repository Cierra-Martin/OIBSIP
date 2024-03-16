import requests
import json
print("Welcome to my weather app")
city=input("Enter the city name: ")
location_key_request= requests.get(f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey=bXaRjHMBGA974phXgLCNnGWdMS7d4Aea&q={city}&language=en-us&details=false")
location_info=json.loads(location_key_request.content)
if location_info:
    location_key=location_info[0]["Key"]
if not location_info:
    print("Invalid city please check your spelling")
daily_forecast_request=requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}?apikey=bXaRjHMBGA974phXgLCNnGWdMS7d4Aea&details=true')
daily_forecast = daily_forecast_request.json() 
print(daily_forecast)   

def weather_forecast(city):
    location_key_request= requests.get(f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey=bXaRjHMBGA974phXgLCNnGWdMS7d4Aea&q={city}&language=en-us&details=false")
    location_info=json.loads(location_key_request.content)
    if location_info:
        location_key=location_info[0]["Key"]
    if not location_info:
        print("Invalid city please check your spelling")
    try:
        daily_forecast_request=requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}?apikey=bXaRjHMBGA974phXgLCNnGWdMS7d4Aea&details=true')
        daily_forecast = daily_forecast_request.json()
        min_temp = daily_forecast['Temperature']('Minimum')('Value')
        max_temp = daily_forecast['Temperature']['Maximum']['Value']
        humidity = daily_forecast['RelativeHumidity']
        weather_condition = daily_forecast['IconPhrase']
        day_precipitation_probability = daily_forecast['DailyForecasts'][0]['Day']['PrecipitationProbability']
        print(f"Today is a {weather_condition} day with a max temp of {max_temp}°C,a min temp of {min_temp}°C a humidity of {humidity}%, and a {day_precipitation_probability}% chance of rain.")
    except Exception as e:
        print("Error: Failed to get weather data")
weather_forecast(city)








       










