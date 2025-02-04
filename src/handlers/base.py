from aiogram.types import Message
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart

from keyboards.inline import keyboard_main, keyboard_type_entry
from main import dp


@dp.message_handler()
async def get_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")


@dp.message_handler(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}!\nВыберите пункт меню",
                         reply_markup=keyboard_main())
