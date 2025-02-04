import asyncio
import logging
import config
from aiogram import Bot, Dispatcher, F

from handlers import appeal, base


async def start():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(levelname)s] %(asctime)s - %(filename)s.%(funcName)s(%(lineno)d): %(message)s"
    )

    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(appeal.router, base.router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
