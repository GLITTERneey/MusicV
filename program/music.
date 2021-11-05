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
                    text="✨gяσυρѕ✨", url=f"https://t.me/{GROUP_SUPPORT}"
                ),
                InlineKeyboardButton(
                    text="✨¢нαηηєℓ✨", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    replied = m.reply_to_message
    chat_id = m.chat.id
    if replied:
        if replied.audio or replied.voice:
            suhu = await replied.reply("📥 **ѕє∂αηg ∂σωηℓσα∂ ѕαвαя ∂υℓυ...**")
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
                    caption=f"💡 **мυѕι¢ ∂ιтαмвαнкαη кє αηтяιαη**\n\n🏷 **ηαмє:** [{songname}]({link})\n💭 **¢нαт:** `{chat_id}`\n🎧 **яєqυєѕт вує:** {m.from_user.mention()}\n🔢 **ѕє∂αηg αηтяι ∂ι ρσѕιѕι »** `{pos}`",
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
                    caption=f"💡 **мυѕι¢ ѕтяєαмιηg ѕтαятℓσѕѕ.**\n\n🏷 **ηαмє:** [{songname}]({link})\n💭 **¢нαт:** `{chat_id}`\n💡 **ѕтαтυѕ:** `Playing`\n🎧 **яєqυєѕт вує:** {m.from_user.mention()}",
                    reply_markup=keyboard,
                )
        else:
            if len(m.command) < 2:
                await m.reply(
                    "» reply to an **αυ∂ισ ƒιℓє** or **gινє ѕσмєтнιηg тσ ѕєαя¢н.**"
                )
            else:
                suhu = await m.reply("🔎 **ѕєαя¢нιηg...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                if search == 0:
                    await suhu.edit("❌ **ησ яєѕυℓтѕ ƒσυη∂.**")
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
                                caption=f"💡 **мυѕι¢ ∂ιтαмвαнкαη кє αηтяιαη**\n\n🏷 **ηαмє:** [{songname}]({url})\n💭 **¢нαт:** `{chat_id}`\n🎧 **яєqυєѕт вує:** {m.from_user.mention()}\n🔢 **ѕє∂αηg αηтяι ∂ι ρσѕιѕι »** `{pos}`",
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
                                    caption=f"💡 **мυѕι¢ ѕтяєαмιηg ѕтαятℓσѕѕ.**\n\n🏷 **ηαмє:** [{songname}]({url})\n💭 **¢нαт:** `{chat_id}`\n💡 **ѕтαтυѕ:** `Playing`\n🎧 **яєqυєѕт вує:** {m.from_user.mention()}",
                                    reply_markup=keyboard,
                                )
                            except Exception as ep:
                                await m.reply_text(f"🚫 error: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply(
                "» reply to an **audio file** or **gινє ѕσмєтнιηg тσ ѕєαя¢н.**"
            )
        else:
            suhu = await m.reply("🔎 **ѕєαя¢нιηg...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:q
                await suhu.edit("❌ **ησ яєѕυℓтѕ ƒσυη∂.**")
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
                            caption=f"💡 **мυѕι¢ ∂ιтαмвαнкαη кє αηтяιαη**\n\n🏷 **ηαмє:** [{songname}]({url})\n💭 **¢нαт:** `{chat_id}`\n🎧 **яєqυєѕт вує:** {m.from_user.mention()}\n🔢 **ѕє∂αηg αηтяι ∂ι ρσѕιѕι »** `{pos}`",
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
                                caption=f"💡 **music streaming startloss.**\n\n🏷 **ηαмє:** [{songname}]({url})\n💭 **¢нαт:** `{chat_id}`\n💡 **𝐒𝐭𝐚𝐭𝐮𝐬:** `Playing`\n🎧 **𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐛𝐲𝐞:** {m.from_user.mention()}",
                                reply_markup=keyboard,
                            )@
                        except Exception as ep:
                            await m.reply_text(f"🚫 error: `{ep}`")


# stream is used for live streaming only

@Client.on_message(command(["stream", f"stream@{BOT_USERNAME}"]) & other_filters)
async def stream(_, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✨gяσυρѕ✨", url=f"https://t.me/{GROUP_SUPPORT}"
                ),
                InlineKeyboardButton(
                    text="✨¢нαηηєℓ✨", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        await m.reply("» give me a live-link/m3u8 url/youtube link to stream.")
    else:"youtube\.com|youtu\.?be)\/.+"
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
                    caption=f"💡 **мυѕι¢ ∂ιтαмвαнкαη кє αηтяιαη**\n\n💭 **chat:** `{chat_id}`\n🎧 **яєqυєѕт вує:** {m.from_user.mention()}\n🔢 **ѕє∂αηg αηтяι ∂ι ρσѕιѕι »** `{pos}`",
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
                        caption=f"💡 **[Radio live]({link}) ѕтяєαм ѕтαятℓσѕѕ.**\n\n💭 **¢нαт:** `{chat_id}`\n💡 **ѕтαтυѕ:** `Playing`\n🎧 **яєqυєѕт вує:** {m.from_user.mention()}",
                        reply_markup=keyboard,
                    )
                except Exception as ep:
                    await m.reply_text(f"🚫 error: `{ep}`")
