# healthy_air_analysis.py
"""
A simple Python script for data analysis.
This script demonstrates basic data logic and prints results to the console.
"""

# Define sample data
temperatures_celsius = [22.5, 23.0, 21.8, 22.2, 23.5]
humidity_percent = [45, 50, 48, 47, 49]

# Calculate average temperature and humidity
avg_temp = sum(temperatures_celsius) / len(temperatures_celsius)
avg_humidity = sum(humidity_percent) / len(humidity_percent)

# Print results
print("HealthyAir Data Analysis Results:")
print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Average Humidity: {avg_humidity:.1f} %")

# Explain script vs notebook
print("\nNote: This script runs from top to bottom and does not keep state between runs. Use scripts for automation and repeatable analysis.")
