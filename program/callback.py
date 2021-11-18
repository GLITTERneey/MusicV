# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **ᴡᴇʟᴄᴏᴍᴇ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) **𝐒𝐚𝐲𝐚 𝐁𝐨𝐭 𝐌𝐮𝐬𝐢𝐜 𝐆𝐫𝐨𝐮𝐩𝐬, 𝐘𝐚𝐧𝐠 𝐁𝐢𝐬𝐚 𝐌𝐞𝐦𝐮𝐭𝐚𝐫 𝐋𝐚𝐠𝐮 𝐃𝐞𝐧𝐠𝐚𝐧 𝐂𝐞𝐩𝐚𝐭 𝐝𝐢 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 𝐃𝐞𝐧𝐠𝐚𝐧 𝐂𝐚𝐫𝐚 𝐘𝐚𝐧𝐠 𝐌𝐮𝐝𝐚𝐡
𝐒𝐚𝐲𝐚 𝐌𝐞𝐦𝐢𝐥𝐢𝐤𝐢 𝐁𝐚𝐧𝐲𝐚𝐤 𝐅𝐢𝐭𝐮𝐫 𝐏𝐫𝐚𝐤𝐭𝐢𝐬 𝐒𝐞𝐩𝐞𝐫𝐭𝐢 :
┏━━━━━━━━━━━━━━
┣• 𝐌𝐞𝐦𝐮𝐭𝐚𝐫 𝐦𝐮𝐬𝐢𝐜.
┣• 𝐌𝐞𝐦𝐮𝐭𝐚𝐫 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠 𝐘𝐨𝐮𝐭𝐮𝐛𝐞.
┣• 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐚𝐠𝐮 𝐀𝐭𝐚𝐮 𝐕𝐢𝐝𝐞𝐨.
┣• 𝐌𝐞𝐦𝐩𝐮𝐧𝐲𝐚𝐢 𝐁𝐚𝐧𝐲𝐚𝐤 𝐌𝐨𝐝𝐮𝐥 𝐌𝐞𝐧𝐚𝐫𝐢𝐤.
┣• 𝐌𝐞𝐧𝐜𝐚𝐫𝐢 𝐋𝐚𝐠𝐮 𝐘𝐚𝐧𝐠 𝐢𝐧𝐠𝐢𝐧 𝐝𝐢 𝐏𝐮𝐭𝐚𝐫 𝐚𝐭𝐚𝐮 𝐝𝐢 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝.
┣• 𝐆𝐮𝐧𝐚𝐤𝐚𝐧 𝐏𝐞𝐫𝐢𝐧𝐭𝐚𝐡 » /start « 𝐮𝐧𝐭𝐮𝐤 𝐌𝐞𝐧𝐠𝐞𝐭𝐚𝐡𝐮𝐢 𝐎𝐧 𝐀𝐭𝐚𝐮 𝐎𝐟 𝐍𝐲𝐚 𝐔𝐬𝐞𝐫𝐛𝐨𝐭. 
┗━━━━━━━━━━━━━━
✨ 𝐓𝐡𝐚𝐧𝐤𝐬 𝐛𝐲𝐞 [𝐆𝐋𝐈𝐓𝐓𝐄𝐑](https://t.me/Biarenakliatnyaaaa) # [𝐋𝐄𝐕𝐈𝐍𝐀](https://t.me/dlwrml) 
🃏 𝐓𝐞𝐫𝐢𝐦𝐚𝐤𝐚𝐬𝐢𝐡 𝐓𝐞𝐥𝐚𝐡 𝐌𝐞𝐧𝐠𝐠𝐮𝐧𝐚𝐤𝐚𝐧 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐈𝐧𝐢! [𝐆𝐋𝐈𝐓𝐓𝐄𝐑](https://t.me/{OWNER_NAME})
━━━━━━━━━━━━━━━**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ᴛᴀᴍʙᴀʜᴋᴀɴ ɢᴜᴀ ᴋᴇ ɢʀᴏᴜᴘs ʟᴜ ᴋɴᴛʟ 🙋‍♂️",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("ʙᴀsɪᴄ ɢᴜɪᴅᴇ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅs", callback_data="cbcmds"),
                    InlineKeyboardButton("ᴅᴏɴᴀᴛᴇ", url=f"https://t.me/Biarenakliatnyaaaa"),
                ],
                [
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘs", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://t.me/TurboGroupSupport"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the basic commands:

» /play (song name/link) - play music on video chat
» /stream (query/link) - stream the yt live/radio live music
» /vplay (video name/link) - play video on video chat
» /vstream - play live video from yt live/m3u8
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link

» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in group)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the admin commands:

» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /volume `1-200` - adjust the volume of music (userbot must be admin)
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
