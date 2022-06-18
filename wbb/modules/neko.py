import os
import nekos
import requests
from PIL import Image
from pyrogram import filters
from pyrogram.types import Message
from wbb import SUDOERS, app
from wbb.core.sections import section
from wbb.utils.dbfunctions import is_gbanned_user, user_global_karma

__MODULE__ = "Neko"
__HELP__ = """
/info [USERNAME|ID] - Get info about a user.
/chat_info [USERNAME|ID] - Get info about a chat.
"""
@app.on_message(filters.command("neko") & ~filters.edited)
async def neko(_, message: Message):
    target = "neko"
    await message.reply_photo(nekos.img(target))
    
@app.on_message(filters.command("awallpaper") & ~filters.edited)
async def awallpaper(_, message: Message):
    target = "wallpaper"
    await message.reply_photo(nekos.img(target))
    
@app.on_message(filters.command("holo") & ~filters.edited)
async def holo(_, message: Message):
    target = "holo"
    await message.reply_photo(nekos.img(target))

@app.on_message(filters.command("poke") & ~filters.edited)
async def poke(_, message: Message):
    reply_text = (
    message.reply_to_message.reply_video if message.reply_to_message else message.reply_video
    )    
    target = "poke"
    reply_text(nekos.img(target))   
