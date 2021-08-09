"""Fun pligon...for HardcoreUserbot
\nCode by @Rambo_86
type `.hellboy` and `.baap` to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="hellboy ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Sunn be lawde")
        await asyncio.sleep(0.7)
        await event.edit("Baap Baap hota h")
        await asyncio.sleep(1)
        await event.edit("Baap ke samne Bakchodi nhi")
        await asyncio.sleep(0.8)
        await event.edit("Aur tera Baap Kaun h janta h na")
        await asyncio.sleep(0.9)
        await event.edit("Nhi janta to jaan le")
        await asyncio.sleep(1)
        await event.edit("Mai hu tera baap")
        await asyncio.sleep(0.8)
        await event.edit("Naam HELLBOY")
        await asyncio.sleep(0.7)
        await event.edit("**HELLBOY PAPA**")
        await asyncio.sleep(1)
        await event.edit("`Abb Nikal yaha se madarchod`")

@borg.on(events.NewMessage(pattern=r"\.baap", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`Ek hi hai baap tum sabka. Naam h HELLBOY `")
    await asyncio.sleep(999)
