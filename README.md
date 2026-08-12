# 🌦️ Real-Time Weather & AQI Analytics Dashboard

A real-time **Weather and Air Quality Analytics Dashboard** that collects live weather and air pollution data for major cities in India, stores the data in a SQLite database, and visualizes it through an interactive **Microsoft Power BI dashboard**.

The project combines **Python automation, REST APIs, SQLite, and Power BI** to provide an easy-to-understand view of temperature, humidity, wind speed, AQI, PM2.5, and PM10 levels.

---

## 📌 Project Overview

Monitoring weather and air quality is important for understanding environmental conditions and their potential impact on daily life.

This project automatically collects data from external APIs and transforms it into meaningful visualizations.

### 🔄 How the system works

```text
Weather & AQI APIs
        ↓
Python Data Collection Script
        ↓
Data Processing
        ↓
SQLite Database
        ↓
Power BI
        ↓
Interactive Dashboard
```

The Python script can be scheduled using **Windows Task Scheduler**, allowing the database to be updated automatically at regular intervals.

---

## ✨ Features

* 🌡️ Real-time weather data collection
* 💨 Air Quality Index (AQI) monitoring
* 🫁 PM2.5 and PM10 monitoring
* 💧 Humidity monitoring
* 🌬️ Wind-speed monitoring
* 🏙️ Supports multiple Indian cities
* 🗄️ SQLite database for data storage
* 📊 Interactive Power BI dashboard
* 📈 Historical trend analysis
* 🔄 Automated data collection
* ⏱️ Scheduled updates using Windows Task Scheduler
* 🔐 API keys stored securely using environment variables
* 📍 City-wise weather and AQI comparison

---

## 🏙️ Cities Covered

The project can collect data for multiple major cities in India, including:

* Delhi
* Mumbai
* Bangalore
* Chennai
* Kolkata
* Hyderabad
* Pune
* Ahmedabad
* Jaipur
* Lucknow
* Kanpur
* Nagpur

Additional cities can easily be added by modifying the city configuration in the Python script.

---

## 🛠️ Technologies Used

| Technology                 | Purpose                          |
| -------------------------- | -------------------------------- |
| **Python**                 | Data collection and processing   |
| **OpenWeatherMap API**     | Weather data                     |
| **AQICN API**              | Air quality data                 |
| **Requests**               | API requests                     |
| **Pandas**                 | Data processing                  |
| **SQLite**                 | Data storage                     |
| **python-dotenv**          | Environment variable management  |
| **Power BI**               | Data visualization and analytics |
| **Windows Task Scheduler** | Automated data collection        |
| **Git & GitHub**           | Version control                  |

---

## 📂 Project Structure

```text
real-time-weather-project/
│
├── scripts/
│   ├── fetch_weather.py
│   └── fetch_weather_aqi.py
│
├── sql/
│   └── weather.db
│
├── powerbi/
│   └── weather_aqi_dashboard.pbix
│
├── .env.sample
├── .gitignore
├── README.md
└── requirements.txt
```

> **Note:** The actual `.env` file containing API keys should never be uploaded to GitHub.

---

## 🔑 API Configuration

This project uses two APIs:

### 1. OpenWeatherMap API

Used to retrieve weather information such as:

* Temperature
* Humidity
* Wind speed
* Weather conditions

### 2. AQICN API

Used to retrieve air quality information such as:

* AQI
* PM2.5
* PM10

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/real-time-weather-project.git
```

Navigate into the project:

```bash
cd real-time-weather-project
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure API keys

Create a `.env` file in the project root:

```env
OWM_KEY=your_openweathermap_api_key
AQI_TOKEN=your_aqicn_api_token
```

Do **not** upload this file to GitHub.

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

## ▶️ Running the Project

After activating the virtual environment and configuring the API keys, run:

```bash
python scripts/fetch_weather_aqi.py
```

The script retrieves the latest weather and AQI information and stores it in the SQLite database.

Example output:

```text
Saved data for Delhi
Saved data for Mumbai
Saved data for Bangalore
Saved data for Chennai
Saved data for Kolkata
```

---

## 🗄️ Database

The project uses **SQLite** to store collected data.

The main table contains fields such as:

```text
id
timestamp
city
temperature
humidity
wind_speed
aqi
pm25
pm10
```

Example database record:

| City   | Temperature | Humidity | Wind Speed | AQI | PM2.5 | PM10 |
| ------ | ----------: | -------: | ---------: | --: | ----: | ---: |
| Delhi  |        28°C |      72% |    3.2 m/s | 145 |    78 |  112 |
| Mumbai |        27°C |      81% |    4.1 m/s |  96 |    43 |   71 |

*Values shown above are examples.*

---

## 📊 Power BI Dashboard

The collected data is connected to **Microsoft Power BI** to create an interactive analytics dashboard.

### Dashboard Components

#### 🌡️ Weather KPIs

* Average Temperature
* Maximum Temperature
* Minimum Temperature
* Average Humidity
* Average Wind Speed

#### 🫁 Air Quality KPIs

* Latest AQI
* Average AQI
* PM2.5
* PM10
* AQI category

#### 📈 Visualizations

* AQI trend over time
* Temperature trend
* City-wise AQI comparison
* City-wise temperature comparison
* Humidity analysis
* PM2.5 and PM10 trends
* KPI cards
* Gauge charts
* Interactive filters

---

## 📅 Historical Analysis

Because the collected information is stored with timestamps, the dashboard can be used to analyze historical trends.

For example:

```text
Time → 08:00 → 08:15 → 08:30 → 08:45 → 09:00
AQI →  120  →  125  →  118  →  130  →  127
```

This makes it possible to observe how environmental conditions change throughout the day.

---

## 🔄 Automated Data Collection

The Python script can be automated using **Windows Task Scheduler**.

For example, the script can be configured to run every **15 minutes**.

```text
08:00 → Fetch data
08:15 → Fetch data
08:30 → Fetch data
08:45 → Fetch data
09:00 → Fetch data
       ↓
SQLite Database
       ↓
Power BI Dashboard
```

This allows the database to continuously collect new observations without manually running the Python script.

---

## 🔐 Security

API credentials are stored using environment variables rather than directly inside Python source code.

Example:

```python
from dotenv import load_dotenv
import os

load_dotenv()

OWM_KEY = os.getenv("OWM_KEY")
AQI_TOKEN = os.getenv("AQI_TOKEN")
```

This prevents sensitive API credentials from being exposed in the GitHub repository.

---

## 📈 Analytics

The dashboard can answer questions such as:

* Which city currently has the highest AQI?
* Which city has the cleanest air?
* How does AQI change throughout the day?
* Which cities have high PM2.5 levels?
* How does temperature vary between cities?
* What is the average humidity?
* How do weather conditions change over time?

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Collect real-time weather data.
2. Collect real-time air quality data.
3. Store environmental data in a structured database.
4. Automate data collection.
5. Analyze historical environmental trends.
6. Build an interactive Power BI dashboard.
7. Provide city-wise environmental insights.

---

## 🚀 Future Enhancements

Possible future improvements include:

* ☁️ Deploying the data collection system to the cloud
* 🤖 Machine learning-based AQI forecasting
* 🔔 Automated AQI alerts and notifications
* 📱 Mobile application
* 🌐 Web-based dashboard
* 🗺️ Interactive geographical AQI map
* 📊 Advanced predictive analytics
* 🧠 Anomaly detection for unusual AQI changes
* ⚡ Real-time streaming using cloud services

---

## 📚 Learning Outcomes

Through this project, the following concepts were implemented:

* REST API integration
* Python automation
* Data extraction
* Data processing with Pandas
* Environment variable management
* SQLite database management
* SQL queries
* Data visualization
* Power BI dashboard development
* DAX measures
* Data analytics
* Windows task automation
* Git and GitHub

---

## 👨‍💻 Author

**Sidharth Joshi**

MCA Student | Data Analytics & Data Science Enthusiast

---

## ⭐ Project

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.
