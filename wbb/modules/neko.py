import os
import html
import nekos
import requests
from PIL import Image
import os
from pyrogram import filters
from pyrogram.types import Message
from wbb import SUDOERS, app

@app.on_message(filters.command("neko") & ~filters.edited)
async def neko(_, message: Message):
    target = "neko"
    await message.reply_photo(nekos.img(target))
    
