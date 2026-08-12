import os
import requests
import pandas as pd
from dotenv import load_dotenv
import datetime
import sqlite3


load_dotenv()
OWM_KEY = os.getenv("OWM_API_KEY")
AQI_KEY = os.getenv("AQICN_API_KEY")


db_path = "../sql/weather.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_aqi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    city TEXT,
    temperature REAL,
    humidity REAL,
    wind_speed REAL,
    aqi INTEGER,
    pm25 REAL,
    pm10 REAL
)
""")
conn.commit()


def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_KEY}&units=metric"
    data = requests.get(url).json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    return temp, humidity, wind


def fetch_aqi(city):
    url = f"https://api.waqi.info/feed/{city}/?token={AQI_KEY}"
    data = requests.get(url).json()
    aqi = data["data"]["aqi"]
    pm25 = data["data"]["iaqi"].get("pm25", {}).get("v", None)
    pm10 = data["data"]["iaqi"].get("pm10", {}).get("v", None)
    return aqi, pm25, pm10


def save_data(city):
    try:
        temp, humidity, wind = fetch_weather(city)
        aqi, pm25, pm10 = fetch_aqi(city)
        timestamp = datetime.datetime.now()

        df = pd.DataFrame([{
            "timestamp": timestamp,
            "city": city,
            "temperature": temp,
            "humidity": humidity,
            "wind_speed": wind,
            "aqi": aqi,
            "pm25": pm25,
            "pm10": pm10
        }])

        df.to_sql("weather_aqi", conn, if_exists="append", index=False)
        print(f"Saved data for {city} at {timestamp}")
    except Exception as e:
        print(f"Error fetching data for {city}: {e}")


if __name__ == "__main__":
    cities = [
    "Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata",
    "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Lucknow",
    "Kanpur", "Nagpur", "Thane", "Bhopal"
]
   
    
    for city in cities:
        save_data(city)

# Close DB connection
conn.close()