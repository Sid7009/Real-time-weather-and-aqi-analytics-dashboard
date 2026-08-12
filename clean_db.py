import sqlite3

# Connect to database
conn = sqlite3.connect("sql/weather.db")

cur = conn.cursor()

# Delete old rows
cur.execute("DELETE FROM weather_aqi")

# Save changes
conn.commit()

print("Old data deleted successfully.")

conn.close()