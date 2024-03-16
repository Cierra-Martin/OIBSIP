from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.title("Weather App")
root.geometry("600x600")
import requests
import json
from io import BytesIO
import datetime
'''
 
Gui Design: input fields, weather data, visual elements

Data visualization: Display weather data in appealing manner using icons or animations

'''
#Entries
city_entry=Entry(root)
city=city_entry.get()

if not city:
    city_entry.delete(0,END)  # Clear previous placeholder text
    city_entry.insert(0, 'Enter City')  # Add placeholder text
    

 # Define the days for the dropdown menu
days = ["Today", "Tomorrow", "Day after tomorrow", "Fourth day", "Fifth day", "Sixth day"]

 # Create a StringVar to hold the selected day
selected_day = StringVar()
selected_day.set(days[0])  # Set the default selected day

# Create the dropdown menu
day_menu = OptionMenu(root, selected_day, *days)
day_menu.grid(row=1,column=2)



def get_weather():
    city=city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city")
        return
    # Get the selected day
    selected = selected_day.get()
    global current_conditions_label
    
    #Get location key
    try:
        location_key_request= requests.get(f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey=bXaRjHMBGA974phXgLCNnGWdMS7d4Aea={city}&language=en-us&details=true")
        location_info=json.loads(location_key_request.content)
        if location_info:
            location_key=location_info[0]["Key"]
     

            current_conditions_request = requests.get(f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey=bXaRjHMBGA974phXgLCNnGWdMS7d4Aea&details=true')
            current_conditions = current_conditions_request.json()
            current_temp_celsius = current_conditions[0]['Temperature']['Metric']['Value']
            current_temp_fahrenheit = current_conditions[0]['Temperature']['Imperial']['Value']
            current_weather_text = current_conditions[0]['WeatherText']
            
            current_conditions_label=Label(root,text=f"Current Temperature: {current_temp_celsius}°C / {current_temp_fahrenheit}°F\nWeather: {current_weather_text}{PhotoImage}")
            current_conditions_label.grid(row=3,column=3,columnspan=4)
            
          
            
            
            hourly_forecast_request = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{location_key}?apikey=bXaRjHMBGA974phXgLCNnGWdMS7d4Aea&details=true')
            hourly_forecast = hourly_forecast_request.json()

            # Extract hour from DateTime and format it
            hourly_forecast_texts = [
                f"{forecast['DateTime'][11:16]}{forecast['IconPhrase']}"
                for forecast in hourly_forecast
            ]

            # Join the hourly forecast texts into a single string
            hourly_forecast_text = '\n'.join(hourly_forecast_texts)

            hourly_wind_speeds = [forecast['Wind']['Speed']['Value'] for forecast in hourly_forecast]
            hourly_wind_speeds_label=Label(root,text="Hourly Wind Speeds:{hourly_wind_speeds}")

            # Display the hourly forecast
            hourly_forecast_label = Label(root, text=hourly_forecast_text)
            hourly_forecast_label.grid(row=5, column=3, columnspan=4)

           

            # Get daily forecast
            
            if selected == "Today":
                daily_forecast_request = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}?apikey=bXaRjHMBGA974phXgLCNnGWdMS7d4Aea&details=true')
            elif selected == "Tomorrow":
                daily_forecast_request = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/2day/{location_key}?apikey=bXaRjHMBGA974phXgLCNnGWdMS7d4Aea&details=true')
            elif selected == "Day after tomorrow":
                daily_forecast_request = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/3day/{location_key}?apikey=bXaRjHMBGA974phXgLCNnGWdMS7d4Aea&details=true')
            # Get daily forecast for the selected day
            if selected == "Fourth day":
                daily_forecast_request = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/4day/{location_key}?apikey=bXaRjHMBGA974phXgLCNnGWdMS7d4Aea&details=true')
            elif selected == "Fifth day":
                daily_forecast_request = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/5day/{location_key}?apikey=bXaRjHMBGA974phXgLCNnGWdMS7d4Aea&details=true')
            elif selected == "Sixth day":
                daily_forecast_request = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/6day/{location_key}?apikey=bXaRjHMBGA974phXgLCNnGWdMS7d4Aea&details=true')
            
            daily_forecast = daily_forecast_request.json()
            daily_forecast_texts =Label(root,[f"{forecast['Date']}: {forecast['Day']}/n['Wind']['Speed']['Value']" for forecast in daily_forecast['DailyForecasts']])
            for i, forecast in enumerate(daily_forecast['DailyForecasts']):
                daily_weather_icon_url = forecast['Day']['Icon']
                daily_weather_icon = download_and_display_icon(daily_weather_icon_url)
                daily_weather_icons[i].config(image=daily_weather_icon)
            # Display weather info
           
            hourly_forecast_texts.config(text='\n'.join(hourly_forecast_texts))
            daily_forecast_texts.config(text='\n'.join(daily_forecast_texts))

           
           
        else:
            messagebox.showerror("Error", "City not found")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

        
def download_and_display_icon(icon_url):
    icon_response = requests.get(icon_url)
    if icon_response.status_code == 200:
        icon_data = icon_response.content
        icon = Image.open(BytesIO(icon_data))
        photo = ImageTk.PhotoImage(icon)
        return photo  
          
    else:
        print("Failed to download weather icon")

daily_weather_icons = []
for i in range(5):
    daily_weather_icon = Label(root)
    daily_weather_icon.grid(row=6, column=i)
    daily_weather_icons.append(daily_weather_icon)



city_label = Label(root, text="Enter city:")
city_label.grid(row=0, column=1, columnspan=2)

city_entry = Entry(root)
city_entry.grid(row=0, column=3, columnspan=2)

get_weather_button = Button(root, text="Get Weather", command=get_weather)
get_weather_button.grid(row=1, column=4, columnspan=2)

















root.mainloop()