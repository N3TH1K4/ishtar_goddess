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
    
