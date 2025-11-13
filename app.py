import requests
import pandas as pd
import matplotlib.pyplot as plt

URL = "https://api.open-meteo.com/v1/forecast"


def get_weather_data(lat, long):
    params = {
        "latitude": lat,
        "longitude": long,
        "hourly": "temperature_2m"
    }
    response = requests.get(URL, params=params)
    data = response.json()

    df = pd.DataFrame({
        "time": data["hourly"]["time"],
        "temperature": data["hourly"]["temperature_2m"]
    })
    df = df.head(24)
    return df


def show_plot(df):
    plt.bar(df['time'], df['temperature'], color='blue')
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.show()


if __name__ == "__main__":
    print("Welcome to Open-Meteo!")
    print("When prompted, please enter the latitude and longitude of where you are and \n"
          "we will show the temparature forecast for the next 24h")

    lat = float(input("Latitude: "))
    long = float(input("Longitude: "))

    df = get_weather_data(lat, long)
    show_plot(df)
