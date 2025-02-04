import asyncio
import logging
from aiogram.types import Message
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from config import BOT_TOKEN, ADMIN_ID
from keyboards.inline import keyboard_main, keyboard_type_entry
from utils.stateform import AppealsForm
from utils.commands import set_commands

dp = Dispatcher()


@dp.startup.register
async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(ADMIN_ID, text=f'[INFO] Бот запущен!')


@dp.shutdown.register
async def stop_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text=f'[INFO] Бот остановлен!')


# @dp.message()
# async def get_start(message: Message):
#     await message.answer(f"Привет, {message.from_user.first_name}!")


async def start():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(levelname)s] %(asctime)s - %(filename)s.%(funcName)s(%(lineno)d): %(message)s"
    )

    bot = Bot(token=BOT_TOKEN)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
