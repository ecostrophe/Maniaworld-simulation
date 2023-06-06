import pandas as pd
import matplotlib.pyplot as plt

# Read data from XLSX file using Pandas
data = pd.read_excel('ManiaData.xlsx', header=0, names=["Num Date", "Num Heure", "Part Day", "Weather", "Temperature", "Humidity", "Precipitation", "Wind Speed", "Atmospheric Pressure"])

# Convert Part Day and Weather columns to categorical data types with specified categories
data["Part Day"] = pd.Categorical(data["Part Day"], categories=["Night", "Morning"])
data["Weather"] = pd.Categorical(data["Weather"], categories=["Rain", "Blow", "Clear", "Normal"])

# Create figure and axis objects
fig, ax = plt.subplots()

# Plot multiple data columns
ax.plot(data["Num Date"], data["Temperature"], label="Temperature")
ax.plot(data["Num Date"], data["Humidity"], label="Humidity")
ax.plot(data["Num Date"], data["Precipitation"], label="Precipitation")
ax.plot(data["Num Date"], data["Wind Speed"], label="Wind Speed")

# Set axis labels and title
ax.set_xlabel("Date")
ax.set_ylabel("Value")
ax.set_title("Data vs. Date")

# Add legend
ax.legend()

# Show plot
plt.show()
