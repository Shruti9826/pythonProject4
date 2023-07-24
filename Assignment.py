import requests

def get_weather_data(location):
    api_key = "b6907d289e10d714a6e88b30761fae22"
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data from the API.")
        return None

def get_temperature_by_date(weather_data, date):
    for forecast in weather_data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['temp']
    return None

def get_wind_speed_by_date(weather_data, date):
    for forecast in weather_data['list']:
        if date in forecast['dt_txt']:
            return forecast['wind']['speed']
    return None

def get_pressure_by_date(weather_data, date):
    for forecast in weather_data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['pressure']
    return None

if __name__ == "__main__":
    location = "London,us"
    weather_data = get_weather_data(location)

    if not weather_data:
        exit()

    while True:
        print("\nChoose an option:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature_by_date(weather_data, date)
            if temperature is not None:
                print(f"Temperature at {date}: {temperature} K")
            else:
                print("Weather data not available for the given date.")

        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed_by_date(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed at {date}: {wind_speed} m/s")
            else:
                print("Wind speed data not available for the given date.")

        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure_by_date(weather_data, date)
            if pressure is not None:
                print(f"Pressure at {date}: {pressure} hPa")
            else:
                print("Pressure data not available for the given date.")

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")