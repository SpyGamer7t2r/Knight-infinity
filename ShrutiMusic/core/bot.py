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
            text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
        )
    except (errors.ChannelInvalid, errors.PeerIdInvalid):
        LOGGER(__name__).error(
            "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel."
        )
        exit()
    except Exception as ex:
        LOGGER(__name__).error(
            f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}."
        )
        exit()

    a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
    if a.status != ChatMemberStatus.ADMINISTRATOR:
        LOGGER(__name__).error(
            "Please promote your bot as an admin in your log group/channel."
        )
        exit()
    LOGGER(__name__).info(f"Music Bot Started as {self.name}")