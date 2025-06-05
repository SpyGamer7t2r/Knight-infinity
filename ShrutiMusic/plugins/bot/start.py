else:
    out = private_panel(_)
    UP, CPU, RAM, DISK = await bot_sys_stats()

    # Try-catch ensures bot won't crash if formatting fails
    try:
        caption = _.get("start_2", "🤖 <b>Bot Online</b>\n\n👤 {0}\n💡 {1}\n\n🟢 Up: {2}\n💽 Disk: {3}\n🧠 CPU: {4}\n📦 RAM: {5}").format(
            message.from_user.mention,
            app.mention,
            UP, DISK, CPU, RAM
        )
    except Exception as e:
        print("⚠️ Caption formatting error:", e)
        caption = "🤖 Bot is alive."

    await message.reply_photo(
        photo="https://telegra.ph/file/36d6a1b0ea34bdfb14f2d.jpg",
        caption=caption,
        reply_markup=InlineKeyboardMarkup(out),
    )

    if await is_on_off(2):
        await app.send_message(
            chat_id=config.LOG_GROUP_ID,
            text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
        )