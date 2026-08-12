import sqlite3

# Connect to database
conn = sqlite3.connect("sql/weather.db")

# Create cursor
cur = conn.cursor()

# Execute query
cur.execute("""
SELECT city, timestamp, aqi
FROM weather_aqi
ORDER BY timestamp DESC
LIMIT 15
""")

# Fetch rows
rows = cur.fetchall()

# Print rows
for row in rows:
    print(row)

# Close connection
conn.close()