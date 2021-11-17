from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Welcome {message.from_user.mention()} !**\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **𝐒𝐚𝐲𝐚 𝐁𝐨𝐭 𝐌𝐮𝐬𝐢𝐜 𝐆𝐫𝐨𝐮𝐩𝐬, 𝐘𝐚𝐧𝐠 𝐁𝐢𝐬𝐚 𝐌𝐞𝐦𝐮𝐭𝐚𝐫 𝐋𝐚𝐠𝐮 𝐃𝐞𝐧𝐠𝐚𝐧 𝐂𝐞𝐩𝐚𝐭 𝐝𝐢 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 𝐃𝐞𝐧𝐠𝐚𝐧 𝐂𝐚𝐫𝐚 𝐘𝐚𝐧𝐠 𝐌𝐮𝐝𝐚𝐡
𝐒𝐚𝐲𝐚 𝐌𝐞𝐦𝐢𝐥𝐢𝐤𝐢 𝐁𝐚𝐧𝐲𝐚𝐤 𝐅𝐢𝐭𝐮𝐫 𝐏𝐫𝐚𝐤𝐭𝐢𝐬 𝐒𝐞𝐩𝐞𝐫𝐭𝐢 :
┏━━━━━━━━━━━━━━
┣• 𝐌𝐞𝐦𝐮𝐭𝐚𝐫 𝐦𝐮𝐬𝐢𝐜.
┣• 𝐌𝐞𝐦𝐮𝐭𝐚𝐫 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠 𝐘𝐨𝐮𝐭𝐮𝐛𝐞.
┣• 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐚𝐠𝐮 𝐀𝐭𝐚𝐮 𝐕𝐢𝐝𝐞𝐨.
┣• 𝐌𝐞𝐦𝐩𝐮𝐧𝐲𝐚𝐢 𝐁𝐚𝐧𝐲𝐚𝐤 𝐌𝐨𝐝𝐮𝐥 𝐌𝐞𝐧𝐚𝐫𝐢𝐤.
┣• 𝐌𝐞𝐧𝐜𝐚𝐫𝐢 𝐋𝐚𝐠𝐮 𝐘𝐚𝐧𝐠 𝐢𝐧𝐠𝐢𝐧 𝐝𝐢 𝐏𝐮𝐭𝐚𝐫 𝐚𝐭𝐚𝐮 𝐝𝐢 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝.
┣• 𝐆𝐮𝐧𝐚𝐤𝐚𝐧 𝐏𝐞𝐫𝐢𝐧𝐭𝐚𝐡 » /start « 𝐮𝐧𝐭𝐮𝐤 𝐌𝐞𝐧𝐠𝐞𝐭𝐚𝐡𝐮𝐢 𝐎𝐧 𝐀𝐭𝐚𝐮 𝐎𝐟 𝐍𝐲𝐚 𝐔𝐬𝐞𝐫𝐛𝐨𝐭. 
┗━━━━━━━━━━━━━━
✨ 𝐓𝐡𝐚𝐧𝐤𝐬 𝐛𝐲𝐞 [𝐆𝐋𝐈𝐓𝐓𝐄𝐑](https://t.me/Biarenakliatnyaaa) # [𝐋𝐄𝐕𝐈𝐍𝐀](https://t.me/dlwrml) 
🃏 𝐓𝐞𝐫𝐢𝐦𝐚𝐤𝐚𝐬𝐢𝐡 𝐓𝐞𝐥𝐚𝐡 𝐌𝐞𝐧𝐠𝐠𝐮𝐧𝐚𝐤𝐚𝐧 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐈𝐧𝐢! [𝐆𝐋𝐈𝐓𝐓𝐄𝐑](https://t.me/{OWNER_NAME})
━━━━━━━━━━━━━━━**
""",
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
                        "sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://t.me/Virtualllnihsad"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ɢʀᴏᴜᴘs", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**ʜᴀʟʟᴏ {message.from_user.mention()}, i'm {BOT_NAME}**\n\n✨ Bot is working normally\n🍀 My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ Bot Version: `v{__version__}`\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 PyTgCalls version: `{pytover.__version__}`\n✨ Uptime Status: `{uptime}`\n\n**Thanks for Adding me here, for playing video & music on your Group's video chat** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
