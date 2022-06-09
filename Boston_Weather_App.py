from tkinter import *

import requests
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz


#####################################################################
# A function to update information
def update():
    timezone = TimezoneFinder()
    # Boston: (Longitude, Latitude) =  (-71.0589, 42.361145)
    place = timezone.timezone_at(lng=-71.0589, lat=42.361145)
    location = pytz.timezone(place)
    time_info = datetime.now(location)
    time = time_info.strftime("%I:%M %p")
    clock_label.config(text="Current Time: ")
    clock_time.config(text=time)

    # get info about weather
    api_from_web = "https://api.openweathermap.org/data/2.5/weather?q=boston&appid={key}"
    data = requests.get(api_from_web).json()
    weather = data['weather'][0]['main']
    temperature = int(data['main']['temp'] - 273.15)
    wind_data = data['wind']['speed']
    humidity_level = data['main']['humidity']
    detailed_weather = data['weather'][0]['description']
    pressure_data = data['main']['pressure']

    # Update information on app
    weather_label.config(text=weather)
    temperature_label.config(text=(temperature, "°"))
    wind_label.config(text=(wind_data, "mph"))
    humidity_label.config(text=(humidity_level, "%"))
    detailed_weather_label.config(text=detailed_weather, anchor=CENTER)
    pressure_label.config(text=(pressure_data, "hPa"))


#########################################################################
# main window
window = Tk()
window.title("Weather App")
window.geometry("900x500+420+200")
window.resizable(False, False)
window.config(background="white")

# Title
title = Label(window, anchor="w", text="Boston Weather App", font=("Bookman Old Style", 25, "bold"), fg="white",
              bg="black", width=16, height=1)
title.place(x=20, y=20)

# Update Button
update_button = Button(text="Update", font=("Bookman Old Style", 16, "bold"), borderwidth=7, cursor="hand2",
                       bg="#f2f2f2", width=12, height=1, command=update)
update_button.place(x=700, y=21)

# Labels for displaying current time
clock_label = Label(window, font=("Times New Roman", 25, "bold"), bg="white")
clock_label.place(x=30, y=400)
clock_time = Label(window, font=("Times New Roman", 25, "bold"), bg="white")
clock_time.place(x=250, y=400)

# Labels for displaying weather and temperature
weather_label = Label(font=("Times New Roman", 35, 'bold'), bg="white")
weather_label.place(x=700, y=180)
temperature_label = Label(font=("Times New Roman", 70, "bold"), fg="#ff6666", bg="white")
temperature_label.place(x=700, y=80)

# Labels for displaying info about wind, humidity level, detailed description, and pressure.
# <wind>
label1_box = Label(width=26, height=6, bg="#e0e0eb")
label1_box.place(x=480, y=280)
label1_textbox = Label(window, text="Wind", font=("Courier", 20, "bold", 'underline'), fg="#19334d", bg="#e0e0eb")
label1_textbox.place(x=530, y=280)
wind_label = Label(text="", font=("Courier", 18, "bold"), fg="#19334d", bg="#e0e0eb")
wind_label.place(x=520, y=327)

# <humidity level>
label2_box = Label(width=26, height=6, bg="#e0e0eb")
label2_box.place(x=700, y=280)
label2_textbox = Label(window, text="Humidity", font=("Courier", 20, "bold", 'underline'), fg="#19334d", bg="#e0e0eb")
label2_textbox.place(x=720, y=280)
humidity_label = Label(text="", font=("Courier", 18, "bold"), fg="#19334d", bg="#e0e0eb")
humidity_label.place(x=750, y=327)

# <detailed_weather>
label3_box = Label(width=26, height=6, bg="#e0e0eb")
label3_box.place(x=480, y=390)
label3_textbox = Label(window, text="Description", font=("Courier", 19, 'bold', 'underline'), fg="#19334d",
                       bg="#e0e0eb")
label3_textbox.place(x=492, y=390)
detailed_weather_label = Label(text="", width=20, font=("Courier", 11, "bold"), fg="#19334d", bg="#e0e0eb",
                               anchor=CENTER)
detailed_weather_label.place(x=480, y=437)

# <pressure>
label4_box = Label(width=26, height=6, bg="#e0e0eb")
label4_box.place(x=700, y=390)
label4_textbox = Label(window, text="Pressure", font=("Courier", 20, 'bold', 'underline'), fg="#19334d", bg="#e0e0eb")
label4_textbox.place(x=722, y=390)
pressure_label = Label(text="", font=("Courier", 18, 'bold'), fg="#19334d", bg="#e0e0eb")
pressure_label.place(x=735, y=437)

# Display time
timezone = TimezoneFinder()
# Boston: (Longitude, Latitude) =  (-71.0589, 42.361145)
place = timezone.timezone_at(lng=-71.0589, lat=42.361145)
location = pytz.timezone(place)
time_info = datetime.now(location)
time = time_info.strftime("%I:%M %p")
clock_label.config(text="Current Time: ")
clock_time.config(text=time)

# Get information
api_from_web = "https://api.openweathermap.org/data/2.5/weather?q=boston&appid={key}"
data = requests.get(api_from_web).json()
weather = data['weather'][0]['main']
temperature = int(data['main']['temp'] - 273.15)
wind_data = data['wind']['speed']
humidity_level = data['main']['humidity']
detailed_weather = data['weather'][0]['description']
pressure_data = data['main']['pressure']

# Display information
weather_label.config(text=weather)
temperature_label.config(text=(temperature, "°"))
wind_label.config(text=(wind_data, "mph"))
humidity_label.config(text=(humidity_level, "%"))
detailed_weather_label.config(text=detailed_weather, anchor=CENTER)
pressure_label.config(text=(pressure_data, "hPa"))


# A function to return current weather
def knowWeather():
    api_data = "https://api.openweathermap.org/data/2.5/weather?q=boston&appid={key}"
    data = requests.get(api_data).json()
    current_weather = data['weather'][0]['main']
    return current_weather


cloud_condition = ["Clouds", "Smoke", "Haze", "Dust", "Fog", "Sand", "Dust", "Ash", "Squall", "Tornado"]
rain_condition = ["Rain", "Thunderstorm", "Drizzle"]

# Display the corresponding icon and picture
if knowWeather() in cloud_condition:
    image1 = PhotoImage(file="weather_condition\\cloud_icon.png")
    cloud_icon = Label(window, image=image1, bg="white")
    cloud_icon.place(x=430, y=30)

    photo1 = PhotoImage(file="weather_condition\\cloudy_boston.png")
    cloudy_photo = Label(window, image=photo1)
    cloudy_photo.place(x=20, y=100)

if knowWeather() == "Clear":
    image2 = PhotoImage(file="weather_condition\\sun_icon.png")
    sun_icon = Label(window, image=image2, bg="white")
    sun_icon.place(x=430, y=30)

    photo2 = PhotoImage(file="C:weather_condition\\sunny_boston.png")
    sunny_photo = Label(window, image=photo2)
    sunny_photo.place(x=20, y=100)

if knowWeather() in rain_condition:
    image3 = PhotoImage(file="weather_condition\\rain_icon.png")
    rain_icon = Label(window, image=image3, bg="white")
    rain_icon.place(x=430, y=30)
    photo3 = PhotoImage(file="weather_condition\\rainy_boston.png")
    rainy_photo = Label(window, image=photo3)
    rainy_photo.place(x=20, y=100)

if knowWeather() == "Snow":
    image4 = PhotoImage(file="weather_condition\\snow_icon.png")
    snow_icon = Label(window, image=image4, bg="white")
    snow_icon.place(x=430, y=30)
    photo4 = PhotoImage(file="weather_condition\\snowy_boston.png")
    snowy_photo = Label(window, image=photo4)
    snowy_photo.place(x=20, y=100)

window.mainloop()
