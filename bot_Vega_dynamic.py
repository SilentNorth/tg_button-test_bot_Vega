from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))

dp = Dispatcher(bot)

countries = {"netherland": {"flag": "\U0001F1F3\U0001F1F1",
                            "ru": "Нидерланды",
                            "sites": {"Ютуб": "https://www.youtube.com/",
                                      "Яндекс": "https://yandex.com/",
                                      "Гугл": "https://www.google.nl/",
                                      "Инста": "https://instagram.com/"}},
             "france": {"flag": "\U0001F1EB\U0001F1F7",
                        "ru": "Франция",
                        "sites": {"Ютуб": "https://www.youtube.com/",
                                  "Яндекс": "https://yandex.com/",
                                  "Гугл": "https://www.google.fr/",
                                  "Инста": "https://instagram.com/"}},
             "spain": {"flag": "\U0001F1EA\U0001F1F8",
                       "ru": "Испания",
                       "sites": {"Ютуб": "https://www.youtube.com/",
                                 "Яндекс": "https://yandex.com/",
                                 "Гугл": "https://www.google.es/",
                                 "Инста": "https://instagram.com/"}},
             "russia": {"flag": "\U0001F1F7\U0001F1FA",
                        "ru": "РФ",
                        "sites": {"Ютуб": "https://www.youtube.com/",
                                  "Яндекс": "https://yandex.ru/",
                                  "Гугл": "https://www.google.ru/",
                                  "Инста": "https://instagram.com/"}},
             "kazakhstan": {"flag": "\U0001F1F0\U0001F1FF",
                            "ru": "Казахстан",
                            "sites": {"Ютуб": "https://www.youtube.com/",
                                      "Яндекс": "https://yandex.kz/",
                                      "Гугл": "https://www.google.kz/",
                                      "instagram": "https://instagram.com/"}},
             "belarus": {"flag": "\U0001F1E7\U0001F1FE",
                         "ru": "Беларусь",
                         "sites": {"Ютуб": "https://www.youtube.com/",
                                   "Яндекс": "https://yandex.by/",
                                   "Гугл": "https://www.google.by/",
                                   "Инста": "https://instagram.com/"}}
         }

kb_countries = InlineKeyboardMarkup()

for key, value in countries.items():
    kb_countries.add(InlineKeyboardButton(text=value["ru"], callback_data=key))

kb_country_sites = {}

for key, value in countries.items():
    keyboard = InlineKeyboardMarkup()
    for inner_key, inner_value in value["sites"].items():
        keyboard.add(InlineKeyboardButton(text=inner_key, url=inner_value))

    kb_country_sites.update({key: keyboard})


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Откуда ты?", reply_markup=kb_countries)


@dp.callback_query_handler(lambda c: c.data in ["netherland", "france", "spain", "russia", "kazakhstan", "belarus"])
async def process_callback_button(callback_query: types.CallbackQuery):

    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text="Вы выбрали страну {}".format(countries[callback_query.data]["flag"]), reply_markup=kb_country_sites[callback_query.data])

if __name__ == "__main__":

    executor.start_polling(dp, skip_updates=True)