
# Weather Forecast Lookup by City or Zip Code

## Overview
This Python program allows users to retrieve current weather information by entering a U.S. ZIP code or a combination of city and state. It performs input validation, fetches geographical coordinates using the OpenCage Geocoding API, and then retrieves weather data from the OpenWeatherMap API.

The output includes location, weather description, temperature, humidity, and other relevant weather data in a user-friendly format.

## Features
- Accepts either ZIP code or city + state input
- Validates input using regular expressions
- Uses OpenCage Geocoding API to retrieve latitude and longitude
- Retrieves current weather data from OpenWeatherMap
- Displays weather conditions, temperature, and location details

## How to Use
1. Obtain API keys for:
   - [OpenCage Geocoder](https://opencagedata.com/)
   - [OpenWeatherMap](https://openweathermap.org/)
2. Add your API keys to the script where prompted.
3. Run the script in a Python environment.
4. Enter either a ZIP code or a city and state as prompted.
5. View the returned weather information.

## Technologies Used
- Python 3.x
- `requests` library
- OpenCage Geocoder API
- OpenWeatherMap API
- `re` for input validation

## Example Output
```
Enter a ZIP code or enter a city and state...
Enter the city: Seattle
Enter the state: WA

Location: Seattle, Washington, United States
Current weather: Clear sky
Temperature: 72.5°F
Humidity: 60%
```

## Author
KR  
Date: May 31, 2023
