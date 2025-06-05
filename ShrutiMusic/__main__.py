import asyncio
 import importlib

from pyrogram import idle from pytgcalls.exceptions import NoActiveGroupCall

import config from ShrutiMusic
 import LOGGER, app, userbot from ShrutiMusic.core.call 
import Aviax from ShrutiMusic.misc import sudo from ShrutiMusic.plugins import ALL_MODULES from ShrutiMusic.utils.database import get_banned_users, get_gbanned from config import BANNED_USERS

async def init(): if not any([config.STRING1, config.STRING2, config.STRING3, config.STRING4, config.STRING5]): LOGGER(name).error("Assistant client variables not defined, exiting...") return

await sudo()

try:
    users = await get_gbanned()
    BANNED_USERS.update(users)

    users = await get_banned_users()
    BANNED_USERS.update(users)
except Exception as e:
    LOGGER(__name__).warning(f"Error fetching banned users: {e}")

await app.start()

for module in ALL_MODULES:
    importlib.import_module("ShrutiMusic.plugins." + module)

LOGGER("ShrutiMusic.plugins").info("Successfully Imported Modules...")

await userbot.start()
await Aviax.start()

try:
    await Aviax.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
except NoActiveGroupCall:
    LOGGER("ShrutiMusic").error(
        "Please turn on the video chat of your log group/channel.\n\nStopping Bot..."
    )
    return
except Exception as e:
    LOGGER("ShrutiMusic").warning(f"Stream call error: {e}")

try:
    await Aviax.decorators()
except Exception as e:
    LOGGER("ShrutiMusic").warning(f"Error while applying decorators: {e}")

LOGGER("ShrutiMusic").info(
    "Shruti Music Started Successfully.\nDon't forget to visit @ShrutiBots"
)

await idle()

await app.stop()
await userbot.stop()
LOGGER("ShrutiMusic").info("Stopping Shruti Music Bot...")

if name == "main": asyncio.run(init())

