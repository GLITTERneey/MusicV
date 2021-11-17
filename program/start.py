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
        f"""✨ **𝐖𝐞𝐥𝐜𝐨𝐦𝐞𝐢𝐧 {message.from_user.mention()} !**\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **𝐒𝐚𝐲𝐚 𝐁𝐨𝐭 𝐌𝐮𝐬𝐢𝐜 𝐆𝐫𝐨𝐮𝐩, 𝐘𝐚𝐧𝐠 𝐁𝐢𝐬𝐚 𝐌𝐞𝐦𝐮𝐭𝐚𝐫 𝐋𝐚𝐠𝐮 𝐃𝐞𝐧𝐠𝐚𝐧 𝐂𝐞𝐩𝐚𝐭 𝐝𝐢 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 𝐃𝐞𝐧𝐠𝐚𝐧 𝐂𝐚𝐫𝐚 𝐘𝐚𝐧𝐠 𝐌𝐮𝐝𝐚𝐡
𝐒𝐚𝐲𝐚 𝐌𝐞𝐦𝐢𝐥𝐢𝐤𝐢 𝐁𝐚𝐧𝐲𝐚𝐤 𝐅𝐢𝐭𝐮𝐫 𝐏𝐫𝐚𝐤𝐭𝐢𝐬 𝐒𝐞𝐩𝐞𝐫𝐭𝐢 :
┏━━━━━━━━━━━━━━
┣• 𝐌𝐞𝐦𝐮𝐭𝐚𝐫 𝐌𝐮𝐬𝐢𝐤.
┣• 𝐌𝐞𝐧𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐚𝐠𝐮.
┣• 𝐌𝐞𝐥𝐢𝐡𝐚𝐭 𝐋𝐢𝐫𝐢𝐤 𝐋𝐚𝐠𝐮.
┣• 𝐌𝐞𝐦𝐢𝐥𝐢𝐤𝐢 𝐁𝐚𝐧𝐲𝐚𝐤 𝐌𝐨𝐝𝐮𝐥 𝐌𝐞𝐧𝐚𝐫𝐢𝐤.
┣• 𝐌𝐞𝐧𝐜𝐚𝐫𝐢 𝐋𝐚𝐠𝐮 𝐘𝐚𝐧𝐠 𝐢𝐧𝐠𝐢𝐧 𝐝𝐢 𝐏𝐮𝐭𝐚𝐫 𝐚𝐭𝐚𝐮 𝐝𝐢 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝.
┣• 𝐆𝐮𝐧𝐚𝐤𝐚𝐧 𝐏𝐞𝐫𝐢𝐧𝐭𝐚𝐡 » /help « 𝐮𝐧𝐭𝐮𝐤 𝐌𝐞𝐧𝐠𝐞𝐭𝐚𝐡𝐮𝐢 𝐅𝐢𝐭𝐮𝐫 𝐋𝐞𝐧𝐠𝐤𝐚𝐩 𝐒𝐚𝐲𝐚
┗━━━━━━━━━━━━━━ 
✨ 𝐓𝐞𝐫𝐢𝐦𝐚𝐊𝐚𝐬𝐢𝐡 𝐓𝐞𝐥𝐚𝐡 𝐌𝐞𝐧𝐠𝐠𝐮𝐧𝐚𝐤𝐚𝐧 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐈𝐧𝐢! [𝐆𝐋𝐈𝐓𝐓𝐄𝐑](https://t.me/Biarenakliatnyaaaa) X [𝐋𝐄𝐕𝐈𝐍𝐀](https://t.me/dlwrml)!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 𝐓𝐚𝐦𝐛𝐚𝐡𝐤𝐚𝐧 𝐆𝐮𝐚 𝐊𝐞 𝐆𝐫𝐨𝐮𝐩 𝐋𝐮 𝐊𝐧𝐭𝐥 🙋‍♂️",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("𝐁𝐚𝐬𝐢𝐜 𝐆𝐮𝐢𝐥𝐝𝐞", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", callback_data="cbcmds"),
                    InlineKeyboardButton("𝐃𝐨𝐧𝐚𝐭𝐮𝐫", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton( 
                        "𝐆𝐫𝐨𝐮𝐩", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton( 
                        "𝐒𝐨𝐫𝐜𝐞 𝐂𝐨𝐝𝐞", url="https://t.me/Biarenakliatnyaaa"
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
                InlineKeyboardButton("𝐆𝐫𝐨𝐮𝐩𝐬", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**нєℓℓσ🙋‍♂️ {message.from_user.mention()}, ι'м {BOT_NAME}**\n\n✨ вσт ιѕ ωσякιηg ησямαℓℓу\n🍀 му мαѕтєя: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ вσт νєяѕιση: `v{__version__}`\n🍀 ρуяσgяαм νєяѕιση: `{pyrover}`\n✨ ρутнση νєяѕιση: `{__python_version__}`\n🍀 ρутg¢αℓℓѕ νєяѕιση: `{pytover.__version__}`\n✨ υρтιмє ѕтαтυѕ: `{uptime}`\n\n**тнαηкѕ ƒσя α∂∂ιηg мє нєяє, ƒσя ρℓαуιηg νι∂єσ & мυѕι¢ ση уσυя gяσυρѕ νι∂єσ ¢нαт** ❤"

    await message.reply_photo(
        photo=f"https://telegra.ph/file/e3687c2f0d0cdf01a83f5.jpg",
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
