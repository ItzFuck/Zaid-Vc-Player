import asyncio
from pytgcalls import idle
from Zaid.main import bot, BOT

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    print("[INFO]: STARTING PYTGCALLSS CLIENT")
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
BOT.run_until_disconnected()
