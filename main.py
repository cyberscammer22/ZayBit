from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Добро пожаловать в ZAYBIT, Снежа бро!")

@dp.message_handler(commands=['crypto'])
async def crypto(message: types.Message):
    await message.reply("BTC сейчас стоит около 66,000$ (заглушка)")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
