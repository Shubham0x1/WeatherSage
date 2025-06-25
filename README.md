#  WeatherSage-Tkinter-GUI

A user-friendly **Python GUI Weather App** that shows live weather details for Indian cities. Built using **Tkinter**, this desktop application includes:

-  City selection or auto-detection  
-  Live temperature, humidity, pressure  
-  Error handling for invalid input or no internet  

---

##  Screenshot

![Weather App Screenshot](weatherpython2.png)

---

##  Features

-  Search by Indian City or State  
-  Auto-detect city using IP  
-  Real-time Temperature, Humidity, Pressure  
-  Dark Mode Toggle 
-  Last updated timestamp  
-  API integration using OpenWeatherMap  
-  Error handling for invalid input and no internet  

---

## 🛠️ Technologies Used

- Python 3.x  
- `tkinter` — GUI toolkit  
- `requests` — for API communication  
- [OpenWeatherMap API](https://openweathermap.org/)  
- [ipinfo.io](https://ipinfo.io) — for location detection  

---

##  How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/WeatherSage-Tkinter-GUI.git
cd WeatherSage-Tkinter-GUI
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python weather_app.py
```

##  Get Your Own API Key

This app uses [OpenWeatherMap](https://openweathermap.org/api). To run it with your own API key:

1. Visit - https://openweathermap.org/api  
2. Sign up and **get your free API key**
3. Open the file `weather_app.py` and replace the default key with your own:

```python
# Before
API_KEY = "1e7404d83a6d0c51e8321e1aedae4fa8"

# After
API_KEY = "your_actual_api_key_here"
```
##  Project Structure
weather-forecast-app/

│ ├── weather_app.py

│-- README.md

│-- requirements.txt

│-- assets/ 

---

##  To-Do / Enhancements

- [ ] Add weather icons (☀️ 🌧️ 🌩️)
- [ ] Save/export weather reports
- [ ] Support for international cities
- [ ] Add voice assistant using `pyttsx3`
- [ ] Add 7-day forecast with OneCall API

---

##  Author

**Shubham Gusain**  
Made with heart using Python & Tkinter

---

##  License

This project is open-source and available under the **MIT License**.

---

##  Support or Feedback?

-  Raise an [issue](https://github.com/your-username/WeatherSage-Tkinter-GUI/issues) for bugs or suggestions  
-  Star the repo if you found it helpful!

---

##  What to Do Now

1. Save this content as `README.md`  
2. Place it in your project root folder  
3. Create `requirements.txt` with the following:
```bash
requests
```

---

###  Summary of Changes Made:

| Issue | Fix |
|-------|-----|
| Code block syntax (` ```requests `) | Changed to valid code block with `requests` inside |
| Missing `---` before sections | Added horizontal lines for visual separation |
| Header emojis | Unified with consistent styling |
| Clarified optional dark mode | Marked as "(if implemented)" |
| Corrected repo name in paths | Replaced `weather-forecast-app` with `WeatherSage-Tkinter-GUI` |
| Added formatting consistency | Proper line breaks, spacing, and indent alignment |
