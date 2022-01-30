import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city,open_weather_token):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city }&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        #pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressyre = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenght_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"])- datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"погода у місті: {city}\n“температура: {cur_weather}C\n"
              f"вологість: {humidity}%\n“тиск: {pressyre} мм.рт.ст\nвітер: {wind} m/c\n"
              f"схід сонця: {sunrise_timestamp}\nзахід сонц€: {sunset_timestamp}\nпродовженність дня: {lenght_of_the_day}\n"
              f"гарного дня"
              )

    except Exception as ex:
        print(ex)
        print("перевірте назву міста")




def main():
    city = input("введіть місто:")
    get_weather(city,open_weather_token)


if __name__ == '__main__':
    main()
