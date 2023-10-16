import asyncio
import logging
from argparse import ArgumentParser
from os import getenv

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

from handlers import menu

from utils import texts

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create a dispatcher instance
dp = Dispatcher()
dp.include_router(menu.router)

# Setup argparse
parser = ArgumentParser()
parser.add_argument("--env", type=str, default=None)

if __name__ == "__main__":
    # Parse arguments
    args = parser.parse_args()
    if args.env:
        load_dotenv(args.env)

    # Start bot
    bot = Bot(token=getenv("BOT_TOKEN"), parse_mode=texts.PARSE_MODE)
    asyncio.run(dp.start_polling(bot))
