import os
import nekos
import requests
from PIL import Image
from pyrogram import filters
from pyrogram.types import Message
from wbb import SUDOERS, app
from wbb.core.sections import section
from wbb.utils.dbfunctions import is_gbanned_user, user_global_karma

__MODULE__ = "Anime Extra"
__HELP__ = """
/neko - Get an image of a Neko (cat girl)
/awallpaper - Get an anime wallpaper
/fgirl - Get an image of a fox girl (kinda looks like neko tho)

"""
@app.on_message(filters.command("neko") & ~filters.edited)
async def neko(_, message: Message):
    target = "neko"
    if message.reply_to_message:
        await message.reply_to_message.reply_photo(nekos.img(target))
    else:
        await message.reply_photo(nekos.img(target))
    
@app.on_message(filters.command("fgirl") & ~filters.edited)
async def fox_girl(_, message: Message):
    target = "fox_girl"
    if message.reply_to_message:
        await message.reply_to_message.reply_photo(nekos.img(target))
    else:
        await message.reply_photo(nekos.img(target))
    

@app.on_message(filters.command("awallpaper") & ~filters.edited)
async def awall(_, message: Message):
    target = "wallpaper"
    if message.reply_to_message:
        await message.reply_to_message.reply_photo(nekos.img(target))
    else:
        await message.reply_photo(nekos.img(target))
        
        
@app.on_message(filters.command("feed") & ~filters.edited)
async def feed(_, message: Message):
    target = "feed"
    if message.reply_to_message:
        await message.reply_to_message.reply_video(nekos.img(target))
    else:
        await message.reply_video(nekos.img(target))
