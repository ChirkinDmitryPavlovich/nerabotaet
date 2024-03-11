from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

API_TOKEN = '6417701016:AAH8f-BHA1KwSLL7fMT7beTR34OdmeLD71w'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("Hello! This is a response to the /start command.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
