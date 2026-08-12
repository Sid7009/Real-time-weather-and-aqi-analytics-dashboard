import os
import requests
from dotenv import load_dotenv

load_dotenv()

AQI_KEY = os.getenv("AQICN_API_KEY")

def get_aqi(city="Delhi"):
    url = f"https://api.waqi.info/feed/{city}/?token={AQI_KEY}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    aqi = get_aqi("Delhi")
    print(aqi)