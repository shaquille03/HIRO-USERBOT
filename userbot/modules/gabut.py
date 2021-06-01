from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio

@register(outgoing=True, pattern="^.amb$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("AMBULANCE")
        sleep(1)
        await e.edit("HARAP")        
        await e.edit("MINGGIR")        
        await e.edit("🔵🔵⬜⬜🔴🔴
🔵🔵⬜⬜🔴🔴")        
        await e.edit("🔴🔴⬜⬜🔵🔵
🔴🔴⬜⬜🔵🔵")        
        await e.edit("🔵🔵⬜⬜🔴🔴
🔵🔵⬜⬜🔴🔴")       
        await e.edit("🔴🔴⬜⬜🔵🔵
🔴🔴⬜⬜🔵🔵")                        
        await e.edit("🔵🔵⬜⬜🔴🔴
🔵🔵⬜⬜🔴🔴")       
        await e.edit("🔴🔴⬜⬜🔵🔵
🔴🔴⬜⬜🔵🔵")
        
