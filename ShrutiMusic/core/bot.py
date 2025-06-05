import uvloop
uvloop.install()

from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config
from ..logging import LOGGER  # Adjust if this import fails

class Aviax(Client):
    def __init__(self):
        LOGGER(__name__).info("Starting Bot...")

        super().__init__(
            name="ShrutiMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()

        me = await self.get_me()
        self.id = me.id
        self.name = me.first_name + " " + (me.last_name or "")
        self.username = me.username
        self.mention = me.mention

        try:
            await self.send_message(
                chat_id=config.LOG_GROUP_ID,
                text=(
                    f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\n"
                    f"🆔 ID: <code>{self.id}</code>\n"
                    f"📝 Name: {self.name}\n"
                    f"🔗 Username: @{self.username}"
                ),
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "[ERROR] Bot can't access the log group. Add the bot and make it admin."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"[ERROR] Log group access failed due to: {type(ex).__name__}."
            )
            exit()

        try:
            member = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error(
                    "[ERROR] Bot is not an admin in the log group. Please promote it."
                )
                exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"[ERROR] Failed to verify admin status: {type(ex).__name__}."
            )
            exit()

        LOGGER(__name__).info(f"✅ Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()