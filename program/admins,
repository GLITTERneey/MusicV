from cache.admins import admins
from driver.veez import call_py
from pyrogram import Client, filters
from driver.decorators import authorized_users_only
from driver.filters import command, other_filters
from driver.queues import QUEUE, clear_queue
from driver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


bttn = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 ɢᴏ ʙᴀᴄᴋ", callback_data="cbmenu")]]
)


bcl = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🗑 ᴄʟᴏsᴇᴅ", callback_data="cls")]]
)


@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "✅ ʙᴏᴛ **ʀᴇʟᴏᴀᴅᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ !**\n✅ **ᴀᴅᴍɪɴ ʟɪsᴛ** ʜᴀs ʙᴇᴇɴ **ᴜᴘᴅᴀᴛᴇᴅ !**"
    )


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="• Mᴇɴᴜ", callback_data="cbmenu"
                ),
                InlineKeyboardButton(
                    text="• Cʟᴏsᴇ", callback_data="cls"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("❌ ᴛɪᴅᴀᴋ ᴀᴅᴀ ʏᴀɴɢ sᴇᴅᴀɴɢ ᴅɪᴘᴜᴛᴀʀ")
        elif op == 1:
            await m.reply("✅ __ǫᴜᴇᴜᴇs__ **ɪs ᴇᴍᴘᴛʏ.**\n\n**• ᴜsᴇʀʙᴏᴛ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ**")
        elif op == 2:
            await m.reply("🗑️ **ᴄʟᴇᴀʀɪɴɢ ᴛʜᴇ ǫᴜᴇᴜᴇs**\n\n**• ᴜsᴇʀʙᴏᴛ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ**")
        else:
            await m.reply_photo(
                photo=f"https://telegra.ph/file/4f6386bb4891938dd7f42.png",
                caption=f"⏭ **ᴅɪʟᴏᴍᴘᴀᴛɪ ᴋᴇ ᴛʀᴇᴋ ʙᴇʀɪᴋᴜᴛɴʏᴀ.**\n\n🏷 **ɴᴀᴍᴇ:** [{op[0]}]({op[1]})\n💭 **ᴄʜᴀᴛ:** `{chat_id}`\n💡 **sᴛᴀᴛᴜs:** `Playing`\n🎧 **ʀᴇǫᴜᴇsᴛ ʙʏᴇ:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **ʟᴀɢᴜ ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ᴀɴᴛʀɪᴀɴ:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["stop", f"stop@{BOT_USERNAME}", "end", f"end@{BOT_USERNAME}", "vstop"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("✅ **sᴛʀᴇᴀᴍɪɴɢ ᴛᴇʟᴀʜ ʙᴇʀᴀᴋʜɪʀ ʙʏᴇ ᴋɴᴛʟ.**")
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ sᴛʀᴇᴀᴍɪɴɢ**")


@Client.on_message(
    command(["pause", f"pause@{BOT_USERNAME}", "vpause"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "⏸ **ᴛʀᴀᴄᴋ ᴘᴀᴜsᴇᴅ.**\n\n• **ᴛᴏ ʀᴇsᴜᴍᴇ ᴛʜᴇ sᴛʀᴇᴀᴍ, ᴜsᴇ ᴛʜᴇ**\n» /resume command."
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ sᴛʀᴇᴀᴍɪɴɢ**")


@Client.on_message(
    command(["resume", f"resume@{BOT_USERNAME}", "vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "▶️ **ᴛʀᴀᴄᴋ ʀᴇsᴜᴍᴇᴅ.**\n\n• **ᴛᴏ ᴘᴀᴜsᴇ ᴛʜᴇ sᴛʀᴇᴀᴍ, ᴜsᴇ ᴛʜᴇ**\n» /pause command."
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ sᴛʀᴇᴀᴍɪɴɢ**")


@Client.on_message(
    command(["mute", f"mute@{BOT_USERNAME}", "vmute"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "🔇 **ᴜsᴇʀʙᴏᴛ ᴍᴜᴛᴇᴅ.**\n\n• **ᴛᴏ ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ, ᴜsᴇ ᴛʜᴇ**\n» /unmute command."
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ sᴛʀᴇᴀᴍɪɴɢ**")


@Client.on_message(
    command(["unmute", f"unmute@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "🔊 **ᴜsᴇʀʙᴏᴛ ᴜɴᴍᴜᴛᴇᴅ.**\n\n• **ᴛᴏ ᴍᴜᴛᴇ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ, ᴜsᴇ ᴛʜᴇ**\n» /mute command."
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ sᴛʀᴇᴀᴍɪɴɢ**")


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 ʜᴀɴʏᴀ ᴀᴅᴍɪɴ ᴅᴇɴɢᴀɴ ɪᴢɪɴ ᴍᴇɴɢᴇʟᴏʟᴀ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴇᴛᴜᴋ ᴛᴏᴍʙᴏʟ ɪɴɪ !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.edit_message_text(
                "⏸ ᴛʜᴇ sᴛʀᴇᴀᴍɪɴɢ ʜᴀs ᴘᴀᴜsᴇᴅ", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ ᴛɪᴅᴀᴋ ᴀᴅᴀ ʏᴀɴɢ sᴇᴅᴀɴɢ sᴛʀᴇᴀᴍɪɴɢ", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 ʜᴀɴʏᴀ ᴀᴅᴍɪɴ ᴅᴇɴɢᴀɴ ɪᴢɪɴ ᴍᴇɴɢᴇʟᴏʟᴀ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴇᴛᴜᴋ ᴛᴏᴍʙᴏʟ ɪɴɪ !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.edit_message_text(
                "▶️ ᴛʜᴇ sᴛʀᴇᴀᴍɪɴɢ ʜᴀs ʀᴇsᴜᴍᴇᴅ", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ ᴛɪᴅᴀᴋ ᴀᴅᴀ ʏᴀɴɢ sᴇᴅᴀɴɢ sᴛʀᴇᴀᴍɪɴɢ", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 ʜᴀɴʏᴀ ᴀᴅᴍɪɴ ᴅᴇɴɢᴀɴ ɪᴢɪɴ ᴍᴇɴɢᴇʟᴏʟᴀ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴇᴛᴜᴋ ᴛᴏᴍʙᴏʟ ɪɴɪ !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text("✅ **sᴛʀᴇᴀᴍɪɴɢ ɪɴɪ ᴛᴇʟᴀʜ ʙᴇʀᴀᴋʜɪʀ ʙʏᴇ**", reply_markup=bcl)
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ ᴛɪᴅᴀᴋ ᴀᴅᴀ ʏᴀɴɢ sᴇᴅᴀɴɢ sᴛʀᴇᴀᴍɪɴɢ", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 ʜᴀɴʏᴀ ᴀᴅᴍɪɴ ᴅᴇɴɢᴀɴ ɪᴢɪɴ ᴍᴇɴɢᴇʟᴏʟᴀ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴇᴛᴜᴋ ᴛᴏᴍʙᴏʟ ɪɴɪ !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "🔇 userbot succesfully muted", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ ᴛɪᴅᴀᴋ ᴀᴅᴀ ʏᴀɴɢ sᴇᴅᴀɴɢ sᴛʀᴇᴀᴍɪɴɢ", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 ʜᴀɴʏᴀ ᴀᴅᴍɪɴ ᴅᴇɴɢᴀɴ ɪᴢɪɴ ᴍᴇɴɢᴇʟᴏʟᴀ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴇᴛᴜᴋ ᴛᴏᴍʙᴏʟ ɪɴɪ !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "🔊 userbot succesfully unmuted", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ ᴛɪᴅᴀᴋ ᴀᴅᴀ ʏᴀɴɢ sᴇᴅᴀɴɢ sᴛʀᴇᴀᴍɪɴɢ", show_alert=True)


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"✅ **ᴠᴏʟᴜᴍᴇ sᴇᴛ ᴛᴏ** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ sᴛʀᴇᴀᴍɪɴɢ**")
