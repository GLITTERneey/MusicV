# Copyright (C) 2021 By VeezMusicProject

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
        f"""✨ **𝐖𝐞𝐥𝐜𝐨𝐦𝐞𝐢𝐧 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝐒𝐚𝐲𝐚 𝐁𝐨𝐭 𝐌𝐮𝐬𝐢𝐜 𝐆𝐫𝐨𝐮𝐩, 𝐘𝐚𝐧𝐠 𝐁𝐢𝐬𝐚 𝐌𝐞𝐦𝐮𝐭𝐚𝐫 𝐋𝐚𝐠𝐮 𝐃𝐞𝐧𝐠𝐚𝐧 𝐂𝐞𝐩𝐚𝐭 𝐝𝐢 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 𝐃𝐞𝐧𝐠𝐚𝐧 𝐂𝐚𝐫𝐚 𝐘𝐚𝐧𝐠 𝐌𝐮𝐝𝐚𝐡
𝐒𝐚𝐲𝐚 𝐌𝐞𝐦𝐢𝐥𝐢𝐤𝐢 𝐁𝐚𝐧𝐲𝐚𝐤 𝐅𝐢𝐭𝐮𝐫 𝐏𝐫𝐚𝐤𝐭𝐢𝐬 𝐒𝐞𝐩𝐞𝐫𝐭𝐢 :
┏━━━━━━━━━━━━━━
┣• 𝐌𝐞𝐦𝐮𝐭𝐚𝐫 𝐌𝐮𝐬𝐢𝐤.
┣• 𝐌𝐞𝐧𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐚𝐠𝐮.
┣• 𝐌𝐞𝐥𝐢𝐡𝐚𝐭 𝐋𝐢𝐫𝐢𝐤 𝐋𝐚𝐠𝐮.
┣• 𝐌𝐞𝐦𝐢𝐥𝐢𝐤𝐢 𝐁𝐚𝐧𝐲𝐚𝐤 𝐌𝐨𝐝𝐮𝐥 𝐌𝐞𝐧𝐚𝐫𝐢𝐤.
┣• 𝐌𝐞𝐧𝐜𝐚𝐫𝐢 𝐋𝐚𝐠𝐮 𝐘𝐚𝐧𝐠 𝐢𝐧𝐠𝐢𝐧 𝐝𝐢 𝐏𝐮𝐭𝐚𝐫 𝐚𝐭𝐚𝐮 𝐝𝐢 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝.
┣• 𝐆𝐮𝐧𝐚𝐤𝐚𝐧 𝐏𝐞𝐫𝐢𝐧𝐭𝐚𝐡 » /help « 𝐮𝐧𝐭𝐮𝐤 𝐌𝐞𝐧𝐠𝐞𝐭𝐚𝐡𝐮𝐢 𝐅𝐢𝐭𝐮𝐫 𝐋𝐞𝐧𝐠𝐤𝐚𝐩 𝐒𝐚𝐲𝐚
┗━━━━━━━━━━━━━━ 
✨ 𝐓𝐞𝐫𝐢𝐦𝐚𝐊𝐚𝐬𝐢𝐡 𝐓𝐞𝐥𝐚𝐡 𝐌𝐞𝐧𝐠𝐠𝐮𝐧𝐚𝐤𝐚𝐧 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐈𝐧𝐢! [𝐆𝐋𝐈𝐓𝐓𝐄𝐑](https://t.me/{OWNER_NAME})!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ тαмвαнкαη ѕαуα кє gяσυρ αη∂α ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ вαѕι¢ gυι∂є", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 ¢σммαη∂ѕ", callback_data="cbcmds"),
                    InlineKeyboardButton(" ∂σηαтυя 🌻", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "✨σƒƒι¢ιαℓ gяσυρ✨", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🌻σƒƒι¢ιαℓ ¢нαηηєℓ🌻", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🤖 ѕσя¢є ¢σ∂є 🤖", url="https://t.me/Biarenakliatnyaaa"
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

1.) **𝐏𝐞𝐫𝐭𝐚𝐦𝐚, 𝐭𝐚𝐦𝐛𝐚𝐡𝐤𝐚𝐧 𝐬𝐚𝐲𝐚 𝐤𝐞 𝐠𝐫𝐮𝐩 𝐀𝐧𝐝𝐚**
2.) **𝐊𝐞𝐦𝐮𝐝𝐢𝐚𝐧, 𝐣𝐚𝐝𝐢𝐤𝐚𝐧 𝐬𝐚𝐲𝐚 𝐬𝐞𝐛𝐚𝐠𝐚𝐢 𝐚𝐝𝐦𝐢𝐧𝐢𝐬𝐭𝐫𝐚𝐭𝐨𝐫 𝐝𝐚𝐧 𝐛𝐞𝐫𝐢𝐤𝐚𝐧 𝐬𝐞𝐦𝐮𝐚 𝐢𝐳𝐢𝐧 𝐤𝐞𝐜𝐮𝐚𝐥𝐢 𝐚𝐝𝐦𝐢𝐧 𝐚𝐧𝐨𝐧𝐢𝐦**
3.) **𝐒𝐞𝐭𝐞𝐥𝐚𝐡 𝐦𝐞𝐦𝐩𝐫𝐨𝐦𝐨𝐬𝐢𝐤𝐚𝐧 𝐬𝐚𝐲𝐚 /reload 𝐝𝐚𝐥𝐚𝐦 𝐠𝐫𝐮𝐩 𝐮𝐧𝐭𝐮𝐤 𝐦𝐞𝐧𝐲𝐞𝐠𝐚𝐫𝐤𝐚𝐧 𝐝𝐚𝐭𝐚 𝐚𝐝𝐦𝐢𝐧**
3.) **𝐓𝐚𝐦𝐛𝐚𝐡𝐤𝐚𝐧 {ASSISTANT_NAME} 𝐤𝐞 𝐠𝐫𝐮𝐩 𝐚𝐭𝐚𝐮 𝐤𝐞𝐭𝐢𝐤 /userbotjoin 𝐀𝐧𝐝𝐚 𝐮𝐧𝐭𝐮𝐤 𝐦𝐞𝐧𝐠𝐮𝐧𝐝𝐚𝐧𝐠𝐧𝐲𝐚**
4.) **𝐍𝐲𝐚𝐥𝐚𝐤𝐚𝐧 𝐨𝐛𝐫𝐨𝐥𝐚𝐧 𝐯𝐢𝐝𝐞𝐨 𝐭𝐞𝐫𝐥𝐞𝐛𝐢𝐡 𝐝𝐚𝐡𝐮𝐥𝐮 𝐬𝐞𝐛𝐞𝐥𝐮𝐦 𝐦𝐮𝐥𝐚𝐢 𝐦𝐞𝐦𝐮𝐭𝐚𝐫 𝐯𝐢𝐝𝐞𝐨/𝐦𝐮𝐬𝐢𝐤**
5.) **𝐊𝐚𝐝𝐚𝐧𝐠-𝐤𝐚𝐝𝐚𝐧𝐠, 𝐦𝐞𝐦𝐮𝐚𝐭 𝐮𝐥𝐚𝐧𝐠 𝐛𝐨𝐭 𝐝𝐞𝐧𝐠𝐚𝐧 𝐦𝐞𝐧𝐠𝐠𝐮𝐧𝐚𝐤𝐚𝐧 /reload 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 𝐝𝐚𝐩𝐚𝐭 𝐦𝐞𝐦𝐛𝐚𝐧𝐭𝐮 𝐀𝐧𝐝𝐚 𝐦𝐞𝐦𝐩𝐞𝐫𝐛𝐚𝐢𝐤𝐢 𝐛𝐞𝐛𝐞𝐫𝐚𝐩𝐚 𝐦𝐚𝐬𝐚𝐥𝐚𝐡**

📌 **𝐉𝐢𝐤𝐚 𝐔𝐬𝐞𝐫𝐁𝐎𝐓 𝐭𝐢𝐝𝐚𝐤 𝐛𝐞𝐫𝐠𝐚𝐛𝐮𝐧𝐠 𝐝𝐞𝐧𝐠𝐚𝐧 𝐨𝐛𝐫𝐨𝐥𝐚𝐧 𝐯𝐢𝐝𝐞𝐨, 𝐩𝐚𝐬𝐭𝐢𝐤𝐚𝐧 𝐚𝐩𝐚𝐤𝐚𝐡 𝐨𝐛𝐫𝐨𝐥𝐚𝐧 𝐯𝐢𝐝𝐞𝐨 𝐬𝐮𝐝𝐚𝐡 𝐝𝐢𝐡𝐢𝐝𝐮𝐩𝐤𝐚𝐧, 𝐚𝐭𝐚𝐮 𝐤𝐞𝐭𝐢𝐤 /userbotleave 𝐤𝐞𝐦𝐮𝐝𝐢𝐚𝐧 /userbotjoin 𝐥𝐚𝐠𝐢**

💡 **𝐉𝐢𝐤𝐚 𝐀𝐧𝐝𝐚 𝐦𝐞𝐦𝐢𝐥𝐢𝐤𝐢 𝐩𝐞𝐫𝐭𝐚𝐧𝐲𝐚𝐚𝐧 𝐭𝐢𝐧𝐝𝐚𝐤 𝐥𝐚𝐧𝐣𝐮𝐭 𝐭𝐞𝐧𝐭𝐚𝐧𝐠 𝐛𝐨𝐭 𝐢𝐧𝐢, 𝐀𝐧𝐝𝐚 𝐝𝐚𝐩𝐚𝐭 𝐦𝐞𝐧𝐜𝐞𝐫𝐢𝐭𝐚𝐤𝐚𝐧𝐧𝐲𝐚 𝐩𝐚𝐝𝐚 𝐨𝐛𝐫𝐨𝐥𝐚𝐧 𝐝𝐮𝐤𝐮𝐧𝐠𝐚𝐧 𝐬𝐚𝐲𝐚 𝐝𝐢 𝐬𝐢𝐧𝐢: @{GROUP_SUPPORT}**

⚡ __𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲𝐞 {BOT_NAME} 𝐀𝐈__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **𝐭𝐞𝐤𝐚𝐧 𝐭𝐨𝐦𝐛𝐨𝐥 𝐝𝐢 𝐛𝐚𝐰𝐚𝐡 𝐮𝐧𝐭𝐮𝐤 𝐦𝐞𝐦𝐛𝐚𝐜𝐚 𝐩𝐞𝐧𝐣𝐞𝐥𝐚𝐬𝐚𝐧 𝐝𝐚𝐧 𝐦𝐞𝐥𝐢𝐡𝐚𝐭 𝐝𝐚𝐟𝐭𝐚𝐫 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 𝐲𝐚𝐧𝐠 𝐭𝐞𝐫𝐬𝐞𝐝𝐢𝐚 !**

⚡ __𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲𝐞 {BOT_NAME} 𝐀𝐈__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 α∂мιη ¢м∂", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 ѕυ∂σ ¢м∂", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 вαѕι¢ ¢м∂", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 gσ вα¢к", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 нєяє ιѕ тнє вαѕι¢ ¢σммαη∂ѕ:

» /play (song name/link) - 𝐩𝐥𝐚𝐲 𝐦𝐮𝐬𝐢𝐜 𝐨𝐧 𝐯𝐢𝐝𝐞𝐨 𝐜𝐡𝐚𝐭
» /stream (query/link) - 𝐬𝐭𝐫𝐞𝐚𝐦 𝐭𝐡𝐞 𝐲𝐭 𝐥𝐢𝐯𝐞/𝐫𝐚𝐝𝐢𝐨/𝐦𝟑𝐮𝟖 𝐥𝐢𝐯𝐞 𝐦𝐮𝐬𝐢𝐜
» /vplay (video name/link) - 𝐩𝐥𝐚𝐲 𝐯𝐢𝐝𝐞𝐨 𝐨𝐧 𝐯𝐢𝐝𝐞𝐨 𝐜𝐡𝐚𝐭
» /vstream - 𝐩𝐥𝐚𝐲 𝐥𝐢𝐯𝐞 𝐯𝐢𝐝𝐞𝐨 𝐟𝐫𝐨𝐦 𝐲𝐭 𝐥𝐢𝐯𝐞/𝐦𝟑𝐮𝟖
» /playlist - 𝐬𝐡𝐨𝐰 𝐲𝐨𝐮 𝐭𝐡𝐞 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭
» /video (query) - 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐯𝐢𝐝𝐞𝐨 𝐟𝐫𝐨𝐦 𝐲𝐨𝐮𝐭𝐮𝐛𝐞
» /song (query) - 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐬𝐨𝐧𝐠 𝐟𝐫𝐨𝐦 𝐲𝐨𝐮𝐭𝐮𝐛𝐞
» /lyric (query) - 𝐬𝐜𝐫𝐚𝐩 𝐭𝐡𝐞 𝐬𝐨𝐧𝐠 𝐥𝐲𝐫𝐢𝐜
» /search (query) - 𝐬𝐞𝐚𝐫𝐜𝐡 𝐚 𝐲𝐨𝐮𝐭𝐮𝐛𝐞 𝐯𝐢𝐝𝐞𝐨 𝐥𝐢𝐧𝐤

» /ping - 𝐬𝐡𝐨𝐰 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐩𝐢𝐧𝐠 𝐬𝐭𝐚𝐭𝐮𝐬
» /uptime - 𝐬𝐡𝐨𝐰 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐮𝐩𝐭𝐢𝐦𝐞 𝐬𝐭𝐚𝐭𝐮𝐬
» /alive - 𝐬𝐡𝐨𝐰 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐚𝐥𝐢𝐯𝐞 𝐢𝐧𝐟𝐨 (𝐢𝐧 𝐠𝐫𝐨𝐮𝐩)

⚡️ __𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲𝐞 {BOT_NAME} αι__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 нєяє ιѕ тнє α∂мιη ¢σммαη∂ѕ:

jeda - 𝐣𝐞𝐝𝐚 𝐬𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠
» /resume - 𝐥𝐚𝐧𝐣𝐮𝐭𝐤𝐚𝐧 𝐬𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠
» /skip - 𝐛𝐞𝐫𝐚𝐥𝐢𝐡 𝐤𝐞 𝐚𝐥𝐢𝐫𝐚𝐧 𝐛𝐞𝐫𝐢𝐤𝐮𝐭𝐧𝐲𝐚
» /stop - 𝐡𝐞𝐧𝐭𝐢𝐤𝐚𝐧 𝐬𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠
» /vmute - 𝐛𝐢𝐬𝐮𝐤𝐚𝐧 𝐛𝐨𝐭 𝐩𝐞𝐧𝐠𝐠𝐮𝐧𝐚 𝐝𝐢 𝐨𝐛𝐫𝐨𝐥𝐚𝐧 𝐬𝐮𝐚𝐫𝐚
» /vunmute - 𝐦𝐞𝐧𝐠𝐚𝐤𝐭𝐢𝐟𝐤𝐚𝐧 𝐬𝐮𝐚𝐫𝐚 𝐛𝐨𝐭 𝐩𝐞𝐧𝐠𝐠𝐮𝐧𝐚 𝐝𝐢 𝐨𝐛𝐫𝐨𝐥𝐚𝐧 𝐬𝐮𝐚𝐫𝐚
» /volume `1-200` - 𝐦𝐞𝐧𝐠𝐚𝐭𝐮𝐫 𝐯𝐨𝐥𝐮𝐦𝐞 𝐦𝐮𝐬𝐢𝐤 (𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐡𝐚𝐫𝐮𝐬 𝐚𝐝𝐦𝐢𝐧)
» /reload - 𝐫𝐞𝐥𝐨𝐚𝐝 𝐛𝐨𝐭 𝐝𝐚𝐧 𝐫𝐞𝐟𝐫𝐞𝐬𝐡 𝐝𝐚𝐭𝐚 𝐚𝐝𝐦𝐢𝐧
» /userbotjoin - 𝐮𝐧𝐝𝐚𝐧𝐠 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐮𝐧𝐭𝐮𝐤 𝐛𝐞𝐫𝐠𝐚𝐛𝐮𝐧𝐠 𝐝𝐞𝐧𝐠𝐚𝐧 𝐠𝐫𝐮𝐩
» /userbotleave - 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡𝐤𝐚𝐧 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐤𝐞𝐥𝐮𝐚𝐫 𝐝𝐚𝐫𝐢 𝐠𝐫𝐮𝐩

⚡️ __𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲𝐞 {BOT_NAME} 𝐀𝐈__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 нєяє ιѕ тнє ѕυ∂σ ¢σммαη∂ѕ:

» /rmw - 𝐜𝐥𝐞𝐚𝐧 𝐚𝐥𝐥 𝐫𝐚𝐰 𝐟𝐢𝐥𝐞𝐬
» /rmd - 𝐜𝐥𝐞𝐚𝐧 𝐚𝐥𝐥 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐟𝐢𝐥𝐞𝐬
» /leaveall - 𝐨𝐫𝐝𝐞𝐫 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐭𝐨 𝐥𝐞𝐚𝐯𝐞 𝐟𝐫𝐨𝐦 𝐚𝐥𝐥 𝐠𝐫𝐨𝐮𝐩

⚡ __𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲𝐞 {BOT_NAME} 𝐀𝐈__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
