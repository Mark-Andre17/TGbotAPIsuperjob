import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove
from secret import *
from states import register_handler_state
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(tg_token)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

register_handler_state(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
