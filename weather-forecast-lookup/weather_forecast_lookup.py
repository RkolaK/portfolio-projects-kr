# Author: KR
# Description: This program will ask the user for their city or zip code,
# request the weather forecast and display the information to the user.
# Date: 5/31/2023

import re
import requests


# Function to validate if it is a valid US zip code with 5 digits
def validate_zip_code(zip_code):
    return re.match(r"^\d{5}$", zip_code)


# Function to validate if it is a valid word for city name
def validate_city(city):
    return re.match(r"^[A-Za-z\s]+$", city)


# Function to validate if it is a valid abbreviation for state
def validate_state(state):
    return re.match(r"^[A-Za-z]{2}$", state)


# Geolocation lookup function by zip code
def geo_lookup_zip(api_key):
    lat, lon = "", ""

    while True:
        # Get user input for the zip code
        zip_code = input("Enter the zip code: ")

        if validate_zip_code(zip_code):
            break
        else:
            print("Invalid zip code. Please enter a valid 5-digit zip code.")

    # Define URL for the API using zip code
    url_zip = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code}," \
              f"US&appid={api_key}"

    # Make the API request
    try:
        response = requests.get(url_zip, timeout=1, verify=True)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err_http:
        print("HTTP Error")
        print(err_http.args[0])
    except requests.exceptions.ReadTimeout as err_timeout:
        print("Time out")
        print("The following exception has been raised: ", err_timeout)
    except requests.exceptions.ConnectionError as err_connect:
        print("Connection error")
        print("The following exception has been raised: ", err_connect)
    except requests.exceptions.RequestException as err_exception:
        print("Exception request")
        print("The following exception has been raised: ", err_exception)
    else:
        # print("The connection was successful.")
        data = response.json()

        # Print data only to verify what was received
        # print(data)

        # Extract the latitude and longitude
        lat = data["lat"]
        lon = data["lon"]

    finally:
        return lat, lon


# Geolocation lookup function by city
def geo_lookup_city(api_key):
    lat, lon = "", ""

    while True:
        # Get the user input for the city name
        city = input("Enter the city name: ")

        if validate_city(city):
            break
        else:
            print("Invalid city name. Please enter an alphabetic city name.")

    while True:
        # Get the user input for the state
        state = input("Enter the state abbreviation: ")

        if validate_state(state):
            break
        else:
            print("Invalid state abbreviation. Please enter a valid two-letter"
                  " state abbreviation.")

    # Define URL for the API using city and state
    url_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city}" \
               f",{state},US&limit=1&appid={api_key}"

    # Make the API request
    try:
        response = requests.get(url_city, timeout=1, verify=True)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err_http:
        print("HTTP Error")
        print(err_http.args[0])
    except requests.exceptions.ReadTimeout as err_timeout:
        print("Time out")
        print("The following exception has been raised: ", err_timeout)
    except requests.exceptions.ConnectionError as err_connect:
        print("Connection error")
        print("The following exception has been raised: ", err_connect)
    except requests.exceptions.RequestException as err_exception:
        print("Exception request")
        print("The following exception has been raised: ", err_exception)
    else:
        # print("The connection was successful.")
        data = response.json()

        # Print data only to verify what was received
        # print(data)

        # Extract the latitude and longitude
        try:
            lat = data[0]["lat"]
            lon = data[0]["lon"]
        except IndexError as err:
            print("An error has occurred. City was not found.")
            print("The following exception has been raised: ", err)
    finally:
        return lat, lon


# Weather lookup function using latitude and longitude
def weather_lookup(api_key, lat, lon, weather_dict):
    while True:
        # Get the user input for unit
        unit = input("Select unit: 'F' for Fahrenheit, 'C' for Celsius or "
                     "'K' for Kelvin: ")

        if unit.upper() == "F":
            unit_selected = "imperial"
            break
        elif unit.upper() == "C":
            unit_selected = "metric"
            break
        elif unit.upper() == "K":
            unit_selected = "standard"
            break
        else:
            print("Invalid unit selection")

    # Define URL for the API using latitude and longitude
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=" \
          f"{lat}&lon={lon}&appid={api_key}&units={unit_selected}"

    # Make the API request
    try:
        response = requests.get(url, timeout=1, verify=True)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err_http:
        print("HTTP Error")
        print(err_http.args[0])
    except requests.exceptions.ReadTimeout as err_timeout:
        print("Time out")
        print("The following exception has been raised: ", err_timeout)
    except requests.exceptions.ConnectionError as err_connect:
        print("Connection error")
        print("The following exception has been raised: ", err_connect)
    except requests.exceptions.RequestException as err_exception:
        print("Exception request")
        print("The following exception has been raised: ", err_exception)
    else:
        # print("The connection was successful.")
        data = response.json()

        # Print data only to verify what was received
        # print(data)

        # Extract the weather data
        weather_dict["current_weather"] = data["weather"][0]["main"]
        weather_dict["description"] = data["weather"][0]["description"]
        weather_dict["current_temp"] = data["main"]["temp"]
        weather_dict["feels_like"] = data["main"]["feels_like"]
        weather_dict["low_temp"] = data["main"]["temp_min"]
        weather_dict["high_temp"] = data["main"]["temp_max"]
        weather_dict["pressure"] = data["main"]["pressure"]
        weather_dict["humidity"] = data["main"]["humidity"]
        weather_dict["clouds"] = data["clouds"]["all"]
        weather_dict["city_name"] = data["name"]
    finally:
        return weather_dict


# Function to print the weather data in a nice format
def pretty_print(weather_data):
    print("\nCURRENT WEATHER FOR", weather_data["city_name"].upper(), ":")
    print("{:<25}{}".format("Current temperature:", str(int(
        weather_data["current_temp"])) + " degrees"))
    print("{:<25}{}".format("Feels like:", str(int(
        weather_data["feels_like"])) + " degrees"))
    print("{:<25}{}".format("High temperature:", str(int(
        weather_data["high_temp"])) + " degrees"))
    print("{:<25}{}".format("Low temperature:", str(int(
        weather_data["low_temp"])) + " degrees"))
    print("{:<25}{}".format("Current weather:", weather_data[
        "current_weather"]))
    print("{:<25}{}".format("Description:", weather_data[
        "description"].title()))
    print("{:<25}{}".format("Cloudiness:", str(int(
        weather_data["clouds"])) + " %"))
    print("{:<25}{}".format("Humidity:", str(int(
        weather_data["humidity"])) + " %"))
    print("{:<25}{}".format("Pressure:", str(int(
        weather_data["pressure"])) + " hPa"))


def main():
    api_key = "api_key"
    weather_dict = {}

    print("Welcome to the weather app!")

    rerun = "Y"
    while rerun.upper() == "Y":
        # Get user input for type of weather lookup - zip code or city or quit
        user_input = input("\nPlease enter '1' for searching weather data "
                           "using zip code, '2' for city, or 'x' to quit: ")
        if user_input == "1":
            lat, lon = geo_lookup_zip(api_key)
        elif user_input == "2":
            lat, lon = geo_lookup_city(api_key)
        elif user_input.lower() == "x":
            break
        else:
            print("Incorrect input. Please try again.")
            continue

        # If lat and lon were found, call weather_lookup and pretty_print
        if lat != "" and lon != "":
            weather_data = weather_lookup(api_key, lat, lon, weather_dict)
            if len(weather_data) != 0:
                pretty_print(weather_data)
        else:
            print("Please try again!")

        # Get user input for rerun the program or quit
        rerun = input("\nWould you like to perform another weather lookup? "
                      "Enter 'Y' to continue or anything else to quit: ")
        if rerun.upper() == "Y":
            continue
        else:
            break

    print('Thanks for using the app!.')


if __name__ == "__main__":
    main()
