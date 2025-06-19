# 🌦️ Tkinter Weather Forecast App

![Weather App Screenshot](weatherpython2.png)

## 📖 Overview

This **Weather Forecast App** is a simple Python GUI application that provides **real-time weather updates** based on user-selected Indian locations. It uses the **OpenWeatherMap API** to fetch data and displays it in a clean and interactive interface built with **Tkinter**.

---

## ✨ Features

- 🎨 User-friendly Tkinter GUI
- 🌐 Real-time weather data using OpenWeatherMap API
- 📊 Displays:
  - Weather climate
  - Description
  - Temperature (in °C)
  - Humidity (%)
  - Atmospheric pressure (mb)
- 🔎 "Search" button to fetch weather info

---

## 🚀 Getting Started

### 1. Clone this Repository
```bash
git clone https://github.com/Shubham0x1/tkinter-weather-app.git
cd tkinter-weather-app

2️⃣ Install the Required Packages

pip install -r requirements.txt

If requirements.txt is not available:
pip install requests python-dotenv

3️⃣ Get Your OpenWeatherMap API Key

Go to: https://home.openweathermap.org/api_keys

Sign in or create a free account

Click “Create Key” and copy your API key

4️⃣ Setup Environment Variables
Create a .env file in your project root folder and add:

API_KEY=your_actual_openweathermap_key_here

5️⃣ Run the Application
python weather_app.py
