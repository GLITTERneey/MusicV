# Copyright (C) 2021 By Veez Music-Project
# Commit Start Date 20/10/2021
# Finished On 28/10/2021

import asyncio
import re

from config import BOT_USERNAME, GROUP_SUPPORT, IMG_1, IMG_2, UPDATES_CHANNEL
from driver.filters import command, other_filters
from driver.queues import QUEUE, add_to_queue
from driver.veez import call_py
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from youtubesearchpython import VideosSearch


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1)
        for r in search.result()["result"]:
            ytid = r["id"]
            if len(r["title"]) > 34:
                songname = r["title"][:60] + "..."
            else:
                songname = r["title"]
            url = f"https://www.youtube.com/watch?v={ytid}"
        return [songname, url]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "bestaudio",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@Client.on_message(command(["play", f"play@{BOT_USERNAME}"]) & other_filters)
async def play(_, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✨𝐆𝐫𝐨𝐮𝐩𝐬✨", url=f"https://t.me/{GROUP_SUPPORT}"
                ),
                InlineKeyboardButton(
                    text="✨𝐂𝐡𝐚𝐧𝐧𝐞𝐥✨", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    replied = m.reply_to_message
    chat_id = m.chat.id
    if replied:
        if replied.audio or replied.voice:
            suhu = await replied.reply("📥 **𝐒𝐞𝐝𝐚𝐧𝐠 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐒𝐚𝐛𝐚𝐫 𝐃𝐮𝐥𝐮...**")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:60] + "..."
                else:
                    songname = replied.audio.file_name[:60] + "..."
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(
                    photo=f"https://telegra.ph/file/ed349acfdc85b6dd88fac.jpg",
                    caption=f"💡 **𝐓𝐫𝐚𝐜𝐤 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨 𝐭𝐡𝐞 𝐪𝐮𝐞𝐮𝐞**\n\n🏷 **𝐍𝐚𝐦𝐞:** [{songname}]({link})\n💭 **𝐂𝐡𝐚𝐭:** `{chat_id}`\n🎧 **𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐛𝐲𝐞:** {m.from_user.mention()}\n🔢 **𝐒𝐞𝐝𝐚𝐧𝐠 𝐀𝐧𝐭𝐫𝐢 𝐃𝐢 𝐏𝐨𝐬𝐢𝐬𝐢 »** `{pos}`",
                    reply_markup=keyboard,
                )
            else:
                await call_py.join_group_call(
                    chat_id,
                    AudioPiped(
                        dl,
                    ),
                    stream_type=StreamType().pulse_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(
                    photo=f"https://telegra.ph/file/ed349acfdc85b6dd88fac.jpg",
                    caption=f"💡 **𝐌𝐮𝐬𝐢𝐜 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠 𝐒𝐭𝐚𝐫𝐭𝐞𝐝.**\n\n🏷 **𝐍𝐚𝐦𝐞:** [{songname}]({link})\n💭 **𝐂𝐡𝐚𝐭:** `{chat_id}`\n💡 **𝐒𝐭𝐚𝐭𝐮𝐬:** `Playing`\n🎧 **𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐛𝐲𝐞:** {m.from_user.mention()}",
                    reply_markup=keyboard,
                )
        else:
            if len(m.command) < 2:
                await m.reply(
                    "» reply to an **audio file** or **give something to search.**"
                )
            else:
                suhu = await m.reply("🔎 **𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                if search == 0:
                    await suhu.edit("❌ **𝐍𝐨 𝐑𝐞𝐬𝐮𝐥𝐭𝐬 𝐟𝐨𝐮𝐧𝐝.**")
                else:
                    songname = search[0]
                    url = search[1]
                    veez, ytlink = await ytdl(url)
                    if veez == 0:
                        await suhu.edit(f"❌ yt-dl issues detected\n\n» `{ytlink}`")
                    else:
                        if chat_id in QUEUE:
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "Audio", 0
                            )
                            await suhu.delete()
                            await m.reply_photo(
                                photo=f"https://telegra.ph/file/ed349acfdc85b6dd88fac.jpg",
                                caption=f"💡 **𝐓𝐫𝐚𝐜𝐤 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨 𝐭𝐡𝐞 𝐪𝐮𝐞𝐮𝐞**\n\n🏷 **𝐍𝐚𝐦𝐞:** [{songname}]({url})\n💭 **𝐂𝐡𝐚𝐭:** `{chat_id}`\n🎧 **𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐛𝐲𝐞:** {m.from_user.mention()}\n🔢 **𝐒𝐞𝐝𝐚𝐧𝐠 𝐀𝐧𝐭𝐫𝐢 𝐃𝐢 𝐏𝐨𝐬𝐢𝐬𝐢 »** `{pos}`",
                                reply_markup=keyboard,
                            )
                        else:
                            try:
                                await call_py.join_group_call(
                                    chat_id,
                                    AudioPiped(
                                        ytlink,
                                    ),
                                    stream_type=StreamType().pulse_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                                await suhu.delete()
                                await m.reply_photo(
                                    photo=f"https://telegra.ph/file/ed349acfdc85b6dd88fac.jpg",
                                    caption=f"💡 **𝐌𝐮𝐬𝐢𝐜 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠 𝐒𝐭𝐚𝐫𝐭𝐞𝐝.**\n\n🏷 **𝐍𝐚𝐦𝐞:** [{songname}]({url})\n💭 **𝐂𝐡𝐚𝐭:** `{chat_id}`\n💡 **𝐒𝐭𝐚𝐭𝐮𝐬:** `Playing`\n🎧 **𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐛𝐲𝐞:** {m.from_user.mention()}",
                                    reply_markup=keyboard,
                                )
                            except Exception as ep:
                                await m.reply_text(f"🚫 error: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply(
                "» reply to an **audio file** or **𝐠𝐢𝐯𝐞 𝐬𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐭𝐨 𝐬𝐞𝐚𝐫𝐜𝐡.**"
            )
        else:
            suhu = await m.reply("🔎 **𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await suhu.edit("❌ **𝐧𝐨 𝐫𝐞𝐬𝐮𝐥𝐭𝐬 𝐟𝐨𝐮𝐧𝐝.**")
            else:
                songname = search[0]
                url = search[1]
                veez, ytlink = await ytdl(url)
                if veez == 0:
                    await suhu.edit(f"❌ yt-dl issues detected\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await suhu.delete()
                        await m.reply_photo(
                            photo=f"https://telegra.ph/file/ed349acfdc85b6dd88fac.jpg",
                            caption=f"💡 **𝐓𝐫𝐚𝐜𝐤 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨 𝐭𝐡𝐞 𝐪𝐮𝐞𝐮𝐞**\n\n🏷 **𝐍𝐚𝐦𝐞:** [{songname}]({url})\n💭 **𝐂𝐡𝐚𝐭:** `{chat_id}`\n🎧 **𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐛𝐲𝐞:** {m.from_user.mention()}\n🔢 **𝐒𝐞𝐝𝐚𝐧𝐠 𝐀𝐧𝐭𝐫𝐢 𝐃𝐢 𝐏𝐨𝐬𝐢𝐬𝐢 »** `{pos}`",
                            reply_markup=keyboard,
                        )
                    else:
                        try:
                            await call_py.join_group_call(
                                chat_id,
                                AudioPiped(
                                    ytlink,
                                ),
                                stream_type=StreamType().pulse_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                            await suhu.delete()
                            await m.reply_photo(
                                photo=f"https://telegra.ph/file/ed349acfdc85b6dd88fac.jpg",
                                caption=f"💡 **𝐦𝐮𝐬𝐢𝐜 𝐬𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠 𝐬𝐭𝐚𝐫𝐭𝐞𝐝.**\n\n🏷 **𝐍𝐚𝐦𝐞:** [{songname}]({url})\n💭 **𝐂𝐡𝐚𝐭:** `{chat_id}`\n💡 **𝐒𝐭𝐚𝐭𝐮𝐬:** `Playing`\n🎧 **𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐛𝐲𝐞:** {m.from_user.mention()}",
                                reply_markup=keyboard,
                            )
                        except Exception as ep:
                            await m.reply_text(f"🚫 error: `{ep}`")


# stream is used for live streaming only

@Client.on_message(command(["stream", f"stream@{BOT_USERNAME}"]) & other_filters)
async def stream(_, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✨𝐆𝐫𝐨𝐮𝐩𝐬✨", url=f"https://t.me/{GROUP_SUPPORT}"
                ),
                InlineKeyboardButton(
                    text="✨𝐂𝐡𝐚𝐧𝐧𝐞𝐥✨", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        await m.reply("» give me a live-link/m3u8 url/youtube link to stream.")
    else:
        link = m.text.split(None, 1)[1]
        suhu = await m.reply("🔄 **𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐬𝐭𝐫𝐞𝐚𝐦...**")

        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, link)
        if match:
            veez, livelink = await ytdl(link)
        else:
            livelink = link
            veez = 1

        if veez == 0:
            await suhu.edit(f"❌ yt-dl issues detected\n\n» `{ytlink}`")
        else:
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, "Radio", livelink, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(
                    photo=f"https://telegra.ph/file/ed349acfdc85b6dd88fac.jpg",
                    caption=f"💡 **𝐓𝐫𝐚𝐜𝐤 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨 𝐭𝐡𝐞 𝐪𝐮𝐞𝐮𝐞**\n\n💭 **𝐂𝐡𝐚𝐭:** `{chat_id}`\n🎧 **𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐛𝐲𝐞:** {m.from_user.mention()}\n🔢 **𝐒𝐞𝐝𝐚𝐧𝐠 𝐀𝐧𝐭𝐫𝐢 𝐃𝐢 𝐏𝐨𝐬𝐢𝐬𝐢 »** `{pos}`",
                    reply_markup=keyboard,
                )
            else:
                try:
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(
                            livelink,
                        ),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(chat_id, "Radio", livelink, link, "Audio", 0)
                    await suhu.delete()
                    await m.reply_photo(
                        photo=f"https://telegra.ph/file/ed349acfdc85b6dd88fac.jpg",
                        caption=f"💡 **[Radio live]({link}) 𝐬𝐭𝐫𝐞𝐚𝐦 𝐬𝐭𝐚𝐫𝐭𝐞𝐝.**\n\n💭 **𝐂𝐡𝐚𝐭:** `{chat_id}`\n💡 **𝐒𝐭𝐚𝐭𝐮𝐬:** `Playing`\n🎧 **𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐛𝐲𝐞:** {m.from_user.mention()}",
                        reply_markup=keyboard,
                    )
                except Exception as ep:
                    await m.reply_text(f"🚫 error: `{ep}`")
