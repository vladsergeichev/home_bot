import config
from aiogram import Router
from aiogram.types import Message
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart

from keyboards.inline import keyboard_main, keyboard_type_entry
from utils.commands import set_commands

router = Router()


@router.startup.register
async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(config.ADMIN_ID, text=f'[INFO] Бот запущен!')


@router.shutdown.register
async def stop_bot(bot: Bot):
    await bot.send_message(config.ADMIN_ID, text=f'[INFO] Бот остановлен!')


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}!\nВыберите пункт меню",
                         reply_markup=keyboard_main())


@router.message()
async def get_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")
