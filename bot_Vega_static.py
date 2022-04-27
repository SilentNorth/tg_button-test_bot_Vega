from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import keyboards
import os

from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))

dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Откуда ты?", reply_markup=keyboards.kb_countries)


@dp.callback_query_handler(lambda c: c.data == "netherland_btn")
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text="Вы выбрали страну \U0001F1F3\U0001F1F1", reply_markup=keyboards.kb_sites_netherland)


@dp.callback_query_handler(lambda c: c.data == "france_btn")
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text="Вы выбрали страну \U0001F1EB\U0001F1F7", reply_markup=keyboards.kb_sites_france)


@dp.callback_query_handler(lambda c: c.data == "spain_btn")
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text="Вы выбрали страну \U0001F1EA\U0001F1F8", reply_markup=keyboards.kb_sites_spain)


@dp.callback_query_handler(lambda c: c.data == "russia_btn")
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text="Вы выбрали страну \U0001F1F7\U0001F1FA", reply_markup=keyboards.kb_sites_russia)


@dp.callback_query_handler(lambda c: c.data == "kazakhstan_btn")
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text="Вы выбрали страну \U0001F1F0\U0001F1FF", reply_markup=keyboards.kb_sites_kazakhstan)


@dp.callback_query_handler(lambda c: c.data == "belarus_btn")
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text="Вы выбрали страну \U0001F1E7\U0001F1FE", reply_markup=keyboards.kb_sites_belarus)

if __name__ == "__main__":

    executor.start_polling(dp, skip_updates=True)