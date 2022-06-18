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
/feed  -  Feed someone by replying
/tickle -  Tickle someone by replying
/slap - Slap someone by replying
/pat - Pat someone by replying
/kiss - Kiss someone by replying
/cuddle - Cuddle Cuddle
/hug - Hug someone by replying
/smug - He He He
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
        await message.reply_to_message.reply_photo(nekos.img(target),caption = "@Goddess_of_War_Rbot")
    else:
        await message.reply_photo(nekos.img(target),caption = "@Goddess_of_War_Rbot")
    

@app.on_message(filters.command("awallpaper") & ~filters.edited)
async def awall(_, message: Message):
    target = "wallpaper"
    if message.reply_to_message:
        await message.reply_to_message.reply_photo(nekos.img(target),caption = "@Goddess_of_War_Rbot")
    else:
        await message.reply_photo(nekos.img(target),caption = "@Goddess_of_War_Rbot")
        
        
@app.on_message(filters.command("feed") & ~filters.edited)
async def feed(_, message: Message):
    target = "feed"
    if message.reply_to_message:
        await message.reply_to_message.reply_video(nekos.img(target))
    else:
        await message.reply_video(nekos.img(target))

@app.on_message(filters.command("tickle") & ~filters.edited)
async def tickle(_, message: Message):
    target = "tickle"
    if message.reply_to_message:
        await message.reply_to_message.reply_video(nekos.img(target))
    else:
        await message.reply_video(nekos.img(target))    
        
@app.on_message(filters.command("slap") & ~filters.edited)
async def slap(_, message: Message):
    target = "slap"
    if message.reply_to_message:
        await message.reply_to_message.reply_video(nekos.img(target))
    else:
        await message.reply_video(nekos.img(target))                

@app.on_message(filters.command("pat") & ~filters.edited)
async def pat(_, message: Message):
    target = "pat"
    if message.reply_to_message:
        await message.reply_to_message.reply_video(nekos.img(target))
    else:
        await message.reply_video(nekos.img(target)) 
        
@app.on_message(filters.command("kiss") & ~filters.edited)
async def kiss(_, message: Message):
    target = "kiss"
    if message.reply_to_message:
        await message.reply_to_message.reply_video(nekos.img(target))
    else:
        await message.reply_video(nekos.img(target))         
  

@app.on_message(filters.command("cuddle") & ~filters.edited)
async def cuddle(_, message: Message):
    target = "cuddle"
    if message.reply_to_message:
        await message.reply_to_message.reply_video(nekos.img(target))
    else:
        await message.reply_video(nekos.img(target))         
        
@app.on_message(filters.command("hug") & ~filters.edited)
async def hug(_, message: Message):
    target = "hug"
    if message.reply_to_message:
        await message.reply_to_message.reply_video(nekos.img(target))
    else:
        await message.reply_video(nekos.img(target))     
        
@app.on_message(filters.command("spank") & ~filters.edited)
async def spank(_, message: Message):
    target = "spank"
    if message.reply_to_message:
        await message.reply_to_message.reply_video(nekos.img(target))
    else:
        await message.reply_video(nekos.img(target))       
        
        
@app.on_message(filters.command("smug") & ~filters.edited)
async def smug(_, message: Message):
    target = "smug"
    if message.reply_to_message:
        await message.reply_to_message.reply_video(nekos.img(target))
    else:
        await message.reply_video(nekos.img(target))                 
