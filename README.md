#  Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates

This Python project monitors weather conditions for multiple cities using the OpenWeatherMap API. It fetches weather data, calculates rollups and aggregates such as average, maximum, and minimum temperatures, and generates alerts based on customizable thresholds. The results are stored as a CSV file, and temperature trends are visualized in bar charts.

## Features
- **Real-time Weather Fetching**: Fetches live weather data from the OpenWeatherMap API for a list of specified cities.
- **Data Aggregation**: Calculates rollups for average, maximum, and minimum temperatures for each city.
## Extra Features
- **Threshold Alerts**: Generates alerts when city temperatures exceed a predefined threshold (default: 30°C).
- **CSV Storage**: Saves daily weather summaries to a CSV file.
- **Data Visualization**: Produces a bar chart showing the temperature trends for the day.
- **Exception Handling**:The script has improved error handling for issues like failed API requests or timeouts, preventing crashes and logging errors when they occur.
 ## Table of Contents
1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)
4. [Output](#output)
5. [Customization](#customization)

## Installation

1. Clone this repository:
  ```
   git clone https://github.com/yourusername/weather-monitoring.git 
   cd weather-monitoring

  ```
 2. Set Up Virtual Environment:
   ```
  
   python -m venv venv 
  
   ```
   ```
   - source venv/bin/activate  # On Windows use `venv\Scripts\activate`

   ```
3. Install the required Python libraries

 ```
   pip install requests pandas matplotlib

 ```
## Configuration
1. API Key: Obtain an API key from OpenWeatherMap by creating a free account.

2. City List:The script fetches data for six cities: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad. You can modify this by editing the CITIES list in the script:
   ```
   CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
   ```
3. API Key Configuration: Replace the placeholder in the script with your actual API key:
   ```
   API_KEY = 'your_api_key_here'
   ```
## Usage
   Run the program using the following command:
   ```
  python weather_monitoring.py
  ```
## How It Works:
  1. The script fetches weather data from the OpenWeatherMap API for the specified cities.
  2. Rollup calculations (average, max, min temperatures) are performed on the fetched data.
  3. Alerts are generated if the temperature for any city exceeds the defined threshold (default: 30°C).
  4. The aggregated data is saved as a CSV file and a bar chart of the temperature trends is created.
## Output
  Alerts
  If a city's temperature exceeds the threshold, an alert will be printed:
  ```
 Alert: Temperature in Delhi exceeds 30°C!
 ```
CSV
 - A daily summary of the weather is saved as daily_weather_summary.csv:
  ```
  daily_weather_summary.csv
  ```
 ```
| City         |    avg_temp      |     max_temp      |   min_temp   | dominant_weather|
|--------------|------------------|-------------------|--------------|-----------------|
|Bangalore     |  23.33           |      23.33        |    23.33     |    Clouds       |
|Chennai       |  28.98           |      28.98        |    28.98     |    Clouds       |
|Delhi         |  29.05           |      29.05        |    29.05     |    Haze         |
|Hyderabad     |  26.23           |      26.23        |    26.23     |    Haze         |
|Kolkata       |  28.97           |      28.97        |    28.97     |    Haze         |
|Mumbai        |  28.99           |      28.99        |    28.99     |    Thunderstorm |
```
Temperature Trend Plot
 - A bar chart representing temperature trends is saved as temperature_trends.png:
   ![weather png](https://github.com/user-attachments/assets/2ce49210-7b64-4a05-a57c-5511ea93330c)
   

## Customization
 1.  Temperature Threshold: To adjust the temperature threshold for alerts, modify the temperature_threshold variable inside the check_alerts() function:   
  ```
  temperature_threshold = 30  # Default is 30°C
  ```
2. Cities: Update the list of cities by modifying the CITIES list:
```
CITIES = ['New York', 'London', 'Tokyo', 'Sydney']
```
3. Polling Interval: Adjust the delay between each API call by modifying the time.sleep() duration:
 ```
 time.sleep(10)  # 10 seconds delay between API requests
 ```


