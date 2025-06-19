from tkinter import *
from tkinter import ttk
import requests
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
api_key = os.getenv("API_KEY")  # API key is securely loaded from .env

# Function to get weather data
def get_report():
    city = city_name.get()
    if not city:
        return  # handle empty city input gracefully
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
        data = response.json()
        if data.get("cod") != 200:
            raise ValueError("Invalid response")

        weather_climate_label1.config(text=data['weather'][0]['main'])
        weather_describtion_label1.config(text=data['weather'][0]['description'])
        temp_label1.config(text=str(round(data['main']['temp'] - 273.15, 3)) + "°C")
        humidity_label1.config(text=str(data['main']['humidity']) + "%")
        pressure_label1.config(text=str(data['main']['pressure']) + "mb")
    except:
        weather_climate_label1.config(text="Error")
        weather_describtion_label1.config(text="Invalid City/API")
        temp_label1.config(text="--")
        humidity_label1.config(text="--")
        pressure_label1.config(text="--")

# Create GUI window
win = Tk()
win.title("Weather Forecast App")
win.config(background="#3498db")
win.geometry('500x500')

# Header
name_label = Label(win, text="Weather App", font=("Roboto", 26, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

# Dropdown for cities
city_name = StringVar()
indian_states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa",
    "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
    "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
    "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]
state_combobox = ttk.Combobox(win, values=indian_states, font=("Roboto", 20), textvariable=city_name)
state_combobox.place(x=50, y=120, height=50, width=400)

# Labels
def create_label(text, y_pos):
    label = Label(win, text=text, font=("Roboto", 16), bg="#3498db", fg="white")
    label.place(x=25, y=y_pos, height=40, width=210)
    value = Label(win, text="", font=("Roboto", 16), bg="#3498db", fg="white")
    value.place(x=245, y=y_pos, height=40, width=210)
    return value

weather_climate_label1 = create_label("Weather Climate:", 260)
weather_describtion_label1 = create_label("Weather Description:", 300)
temp_label1 = create_label("Temperature:", 340)
humidity_label1 = create_label("Humidity:", 380)
pressure_label1 = create_label("Pressure:", 420)

# Search button
search_button = Button(win, text="Search", font=("Roboto", 18), bg="Red", fg="white", borderwidth=2, command=get_report)
search_button.place(x=70, y=200, height=50, width=360)

# Run app
win.mainloop()
