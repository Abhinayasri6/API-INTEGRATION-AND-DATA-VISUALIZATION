import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Fetch Data from the API
url = "https://api.open-meteo.com/v1/forecast?latitude=17.385&longitude=78.4867&hourly=temperature_2m,precipitation,wind_speed_10m"
response = requests.get(url)
data = response.json()

# Step 2: Convert to DataFrame and Select relevant weather data
df = pd.DataFrame(data['hourly'])

# Step 3: Plot the Data using Seaborn
sns.set(style="whitegrid")

# Convert 'time' to datetime objects
df['time'] = pd.to_datetime(df['time'])

# Plotting temperature
plt.figure(figsize=(15, 7))
sns.lineplot(x='time', y='temperature_2m', data=df)
plt.title("Hourly Temperature (2m)")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
