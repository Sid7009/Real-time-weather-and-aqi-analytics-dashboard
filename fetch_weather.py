import os
import requests
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

OWM_KEY = os.getenv("OWM_API_KEY")

def get_weather(city="Delhi"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    weather = get_weather("Delhi")
    print(weather)
