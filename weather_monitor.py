import requests                 # For making API requests
import pandas as pd              # For handling data in a structured way
from datetime import datetime, timezone  # For handling date and time
import time                             # For adding delays
import matplotlib.pyplot as plt        # For plotting data


API_KEY = 'Replace with your actual API key'          
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']  # List of cities to fetch weather data for
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"   # Base URL for the OpenWeatherMap API

daily_weather = []      # List to store weather data for the day
alerts = []  # List to store alerts for temperature thresholds

def get_weather_data(city):
    """Fetch weather data for a given city from OpenWeatherMap API."""
    try:         # Making a GET request to the API with a timeout of 15 seconds

        response = requests.get(BASE_URL.format(city, API_KEY), timeout=15)  # Set timeout for requests
        data = response.json()   # Convert the response to JSON format
        if response.status_code == 200:  # Check if the request was successful
            return {
                'city': city,
                'main': data['weather'][0]['main'],   # Main weather condition
                'temp': data['main']['temp'] - 273.15,  # Convert Kelvin to Celsius
                'feels_like': data['main']['feels_like'] - 273.15,   # Convert feels like temperature
                'humidity': data['main']['humidity'],          # Humidity percentage
                'wind_speed': data['wind']['speed'],           # Wind speed
                'dt': datetime.fromtimestamp(data['dt'], timezone.utc).strftime('%Y-%m-%d %H:%M:%S')      # Formatted date and time
            }
        else:
        # Print error message if the request failed

            print(f"Error fetching data for {city}: {data.get('message', 'No error message provided')}")
            return None
    except Exception as e:             
            # Print exception message if an error occurs during the request
        print(f"Exception occurred while fetching data for {city}: {e}")
        return None

def process_weather_data():
    """Process weather data for all cities."""
    for city in CITIES:       # Loop through each city
        weather = get_weather_data(city)    # Fetch weather data
        if weather:     # Check if weather data was successfully fetched
            daily_weather.append(weather) # Append weather data to daily_weather list
            print(f"Weather data for {city}: {weather}")  # Debug print
            check_alerts(weather)  # Check for alerts
        else:
            print(f"Failed to get weather data for {city}")  # Debug print # Debug print for failure

def check_alerts(weather):
    """Check if the weather data exceeds predefined alert conditions."""
    temperature_threshold = 30   # Set temperature threshold for alerts (in Celsius)
    print(f"Temperature in {weather['city']}: {weather['temp']:.2f}°C")  # Debug print
    if weather['temp'] > temperature_threshold:    # Check if temperature exceeds threshold
        alert_message = f"Alert: Temperature in {weather['city']} exceeds {temperature_threshold}°C!"
        print(alert_message)           # Print alert message
        alerts.append(alert_message)  # Store alert message in alerts list

def calculate_daily_summary():
    """Calculate daily summary statistics from the weather data."""
    df = pd.DataFrame(daily_weather)   # Convert daily_weather list to DataFrame
    summary = df.groupby('city').agg(  # Group by city and calculate statistics
        avg_temp=('temp', 'mean'),     # Average temperature
        max_temp=('temp', 'max'),     # Maximum temperature
        min_temp=('temp', 'min'),     # Minimum temperature
        dominant_weather=('main', lambda x: x.mode()[0])   # Most common weather condition
    )
    print("Daily summary:")   # Debug print
    print(summary)            # Print daily summary
    return summary            # Return the summary DataFrame

def save_daily_summary_to_csv(summary, filename='daily_weather_summary.csv'):
    """Save the daily weather summary to a CSV file."""
    summary.to_csv(filename)                # Save summary to CSV
    print(f"Daily summary saved to {filename}")        # Confirmation print

def plot_temperature_trends(summary):
    """Plot temperature trends for each city."""
    ax = summary.plot(y=['avg_temp', 'max_temp', 'min_temp'], kind='bar')  # Create a bar plot 
    plt.title('Daily Temperature Summary')      # Set plot title
    plt.xlabel('City')                          # Set x-axis label
    plt.ylabel('Temperature (°C)')              # Set y-axis label  
    plt.tight_layout()                          # Adjust layout
    plt.savefig('temperature_trends.png')  # Save the plot to a file instead of showing
    plt.close()  # Close the plot to avoid blocking the script

def print_alerts():
    """Print all alerts generated during the data processing."""
    if alerts:            # Check if there are any alerts
        print("\n--- Alerts Summary ---")
        for alert in alerts:   # Loop through and print each alert
            print(alert)
    else:
        print("No alerts today.")      # Print if no alerts were generated

if __name__ == "__main__":
    iterations = 2  # Set how many times to fetch data
    try:
        for _ in range(iterations):
            print("\nFetching weather data...")
            process_weather_data()   # Process weather data for all cities
            time.sleep(10)  # Wait for 10 seconds for testing

            if len(daily_weather) > 0:  # Check if daily_weather has entries
                daily_summary = calculate_daily_summary() # Calculate daily summary
                save_daily_summary_to_csv(daily_summary)  # Save summary to CSV
                plot_temperature_trends(daily_summary)  # Plot the trends
                print("Daily summary calculated")  # Debug print
                print_alerts()  # Print alerts at the end of the day
                daily_weather.clear()  # Reset daily weather data for the next iteration
                alerts.clear()  # Clear alerts for the new iteration
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        print_alerts()  # Print any alerts before exiting
    except Exception as e:
        print(f"An error occurred: {e}")  # Print any exceptions that occur
