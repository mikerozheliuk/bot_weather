import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("ѕрив≥т напиши мен≥ назву м≥ста ≥ € пришлю свою погоду!!!! ")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text }&appid={open_weather_token}&units=metric"
        )
        data = r.json()


        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressyre = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenght_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"])- datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f"ѕогода у м≥ст≥: {city}\n“емпература: {cur_weather}C\n"
                            f"¬олог≥сть: {humidity}%\n“иск: {pressyre} мм.рт.ст\n¬≥тер: {wind} m/c\n"
                            f"—х≥д сонц€: {sunrise_timestamp}\nзах≥д сонц€: {sunset_timestamp}\nпродовженн≥сть дн€: {lenght_of_the_day}\n"
                            f"√арного дн€"
                            )

    except:
        await message.reply("ѕерев≥рте назву м≥ста")


if __name__ == '__main__':
    executor.start_polling(dp)
