"""
Author: LeoChoco
CreatTime: 2022/12/25 12:22
Description: ...
"""
import os
import logging
import os.path
import random

from khl import Bot, Message, MessageTypes

from pic_repo.constance import PIC_PATH
from src.yukari_api import get_picture_from_yukari

logging.basicConfig(level='INFO')
# 推荐使用 os.path 来解决这种 hardcoded path 问题
with open('./token.txt', 'r', encoding='utf-8') as file:
    token = file.read()

bot = Bot(token=token)


# register command, send `/hello` in channel to invoke

@bot.command(name='来点涩图')
async def multimedia(msg: Message):
    pic_name = get_picture_from_yukari()
    img_url = await bot.client.create_asset(os.path.join(PIC_PATH, pic_name))
    await msg.ctx.channel.send(img_url, type=MessageTypes.IMG)


# everything done, go ahead now!
bot.run()
# now invite the bot to a server, and send '/hello' in any channel
# (remember to grant the bot with read & send permissions)
