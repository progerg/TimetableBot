from vkbottle.bot import Bot, Message

from blueprints import bps
from config import *
import asyncio

import time
from models.db_session import global_init


loop = asyncio.get_event_loop()
loop.create_task(global_init(DB_LOGIN, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME))

bot = Bot(token=TOKEN)

for bp in bps:
    bp.load(bot)

bot.run_forever()
