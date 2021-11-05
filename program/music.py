# Copyright (C) 2021 By Veez Music-Project
# Commit Start Date 20/10/2021
# Finished On 28/10/2021

import asyncio
import re

from config import ASSISTANT_NAME, BOT_USERNAME, IMG_1, IMG_2
from driver.filters import command, other_filters
from driver.queues import QUEUE, add_to_queue
from driver.veez import call_py, user
from pyrogram import Client
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
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
                songname = r["title"][:70]
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
async def play(c: Client, m: Message):
    replied = m.reply_to_message
    chat_id = m.chat.id
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="• мєηυ", callback_data="cbmenu"),
                InlineKeyboardButton(text="• ¢ℓσѕє∂", callback_data="cls"),
            ]
        ]
    )
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 υηтυк мєηggυηαкαη ѕαуα, ѕαуα нαяυѕ мєηʝα∂ι **α∂мιηιѕтяαтσя** ∂єηgαη вєяιкυт ιηι **ρєямιѕѕισηѕ**:\n\n» ❌ __Delete messages__\n» ❌ __Restrict users__\n» ❌ __Add users__\n» ❌ __Manage video chat__\n\nData is **updated** automatically after you **promote me**"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "тι∂αк α∂α ιzιη уαηg ∂ιρєяℓυкαη:" + "\n\n» ❌ __Manage video chat__"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "тι∂αк α∂α ιzιη уαηg ∂ιρєяℓυкαη:" + "\n\n» ❌ __Delete messages__"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("тι∂αк α∂α ιzιη уαηg ∂ιρєяℓυкαη:" + "\n\n» ❌ __Add users__")
        return
    if not a.can_restrict_members:
        await m.reply_text("тι∂αк α∂α ιzιη уαηg ∂ιρєяℓυкαη:" + "\n\n» ❌ __Restrict users__")
        return
    try:
        ubot = await user.get_me()
        b = await c.get_chat_member(chat_id, ubot.id)
        if b.status == "kicked":
            await m.reply_text(
                f"@{ASSISTANT_NAME} **∂ι вαηηє∂ ∂ι gяσυρ ιηι** {m.chat.title}\n\n» **υηвαη υѕєявσт тєяℓєвιн ∂αнυℓυ ʝιкα ιηgιη мєηggυηαкαη вσт ιηι.**"
            )
            return
    except UserNotParticipant:
        if m.chat.username:
            try:
                await user.join_chat(m.chat.username)
            except Exception as e:
                await m.reply_text(f"❌ **υѕєявσт gαgαℓ вєяgαвυηg**\n\n**reason**:{e}")
                return
        else:
            try:
                pope = await c.export_chat_invite_link(chat_id)
                pepo = await c.revoke_chat_invite_link(chat_id, pope)
                await user.join_chat(pepo.invite_link)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await m.reply_text(
                    f"❌ **υѕєявσт gαgαℓ вєяgαвυηg**\n\n**reason**:{e}"
                )

    if replied:
        if replied.audio or replied.voice:
            suhu = await replied.reply("📥 **∂σωηℓσα∂ιηg αυ∂ισ...**")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:70]
                else:
                    if replied.audio.file_name:
                        songname = replied.audio.file_name[:70]
                    else:
                        songname = "Audio"
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **ℓα¢αк ∂ιтαмвαнкαη кє αηтяєαη**\n\n🏷 **ηαмє:** [{songname}]({link})\n💭 **¢нαт:** `{chat_id}`\n🎧 **яєqυєѕт вує:** {m.from_user.mention()}\n🔢 **αηтяι ∂ι ρσѕιѕι »** `{pos}`",
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
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{IMG_2}",
                    caption=f"💡 **ѕтяєαмιηg мυѕιк ∂ιмυℓαι.**\n\n🏷 **ηαмє:** [{songname}]({link})\n💭 **¢нαт:** `{chat_id}`\n💡 **ѕтαтυѕ:** `Playing`\n🎧 **яєqυєѕт вує:** {requester}",
                    reply_markup=keyboard,
                )
        else:
            if len(m.command) < 2:
                await m.reply(
                    "» яєρℓу тσ αη **αυ∂ισ ƒιℓє** σя **вєяιкαη ѕєѕυαтυ υηтυк ∂ι¢αяι.**"
                )
            else:
                suhu = await m.reply("🔎 **ѕєαя¢нιηg...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                if search == 0:
                    await suhu.edit("❌ **no results found.**")
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
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=f"{IMG_1}",
                                caption=f"💡 **ℓα¢αк ∂ιтαмвαнкαη кє αηтяєαη**\n\n🏷 **ηαмє:** [{songname}]({url})\n💭 **¢нαт:** `{chat_id}`\n🎧 **яєqυєѕт вує:** {requester}\n🔢 **αηтяι ∂ι ρσѕιѕι »** `{pos}`",
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
                                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                                await m.reply_photo(
                                    photo=f"{IMG_2}",
                                    caption=f"💡 **ѕтяєαмιηg мυѕιк ∂ιмυℓαι.**\n\n🏷 **ηαмє:** [{songname}]({url})\n💭 **¢нαт:** `{chat_id}`\n💡 **ѕтαтυѕ:** `Playing`\n🎧 **яєqυєѕт вує:** {requester}",
                                    reply_markup=keyboard,
                                )
                            except Exception as ep:
                                await m.reply_text(f"🚫 error: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply(
                "» яєρℓу тσ αη **αυ∂ισ ƒιℓє** σя **вєяιкαη ѕєѕυαтυ υηтυк ∂ι¢αяι.**"
            )
        else:
            suhu = await m.reply("🔎 **ѕєαя¢нιηg...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await suhu.edit("❌ **no results found.**")
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
                        requester = (
                            f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                        )
                        await m.reply_photo(
                            photo=f"{IMG_1}",
                            caption=f"💡 **ℓα¢αк ∂ιтαмвαнкαη кє αηтяєαη**\n\n🏷 **ηαмє:** [{songname}]({url})\n💭 **¢нαт:** `{chat_id}`\n🎧 **яєqυєѕт вує:** {requester}\n🔢 **αηтяι ∂ι ρσѕιѕι »** `{pos}`",
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
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=f"{IMG_2}",
                                caption=f"💡 **music streaming started.**\n\n🏷 **Name:** [{songname}]({url})\n💭 **Chat:** `{chat_id}`\n💡 **Status:** `Playing`\n🎧 **Request by:** {requester}",
                                reply_markup=keyboard,
                            )
                        except Exception as ep:
                            await m.reply_text(f"🚫 error: `{ep}`")


# stream is used for live streaming only


@Client.on_message(command(["stream", f"stream@{BOT_USERNAME}"]) & other_filters)
async def stream(c: Client, m: Message):
    chat_id = m.chat.id
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="• мєηυ", callback_data="cbmenu"),
                InlineKeyboardButton(text="• ¢ℓσѕє∂", callback_data="cls"),
            ]
        ]
    )
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 υηтυк мєηggυηαкαη ѕαуα, ѕαуα нαяυѕ мєηʝα∂ι **α∂мιηιѕтяαтσя** ∂єηgαη вєяιкυт ιηι **ρєямιѕѕισηѕ**:\n\n» ❌ __Delete messages__\n» ❌ __Restrict users__\n» ❌ __Add users__\n» ❌ __Manage video chat__\n\nData is **updated** automatically after you **promote me**"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "тι∂αк α∂α ιzιη уαηg ∂ιρєяℓυкαη:" + "\n\n» ❌ __Manage video chat__"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "тι∂αк α∂α ιzιη уαηg ∂ιρєяℓυкαη:" + "\n\n» ❌ __Delete messages__"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("тι∂αк α∂α ιzιη уαηg ∂ιρєяℓυкαη:" + "\n\n» ❌ __Add users__")
        return
    if not a.can_restrict_members:
        await m.reply_text("тι∂αк α∂α ιzιη уαηg ∂ιρєяℓυкαη:" + "\n\n» ❌ __Restrict users__")
        return
    try:
        ubot = await user.get_me()
        b = await c.get_chat_member(chat_id, ubot.id)
        if b.status == "kicked":
            await m.reply_text(
                f"@{ASSISTANT_NAME} **∂ι вαηηє∂ ∂ι gяσυρ ιηι** {m.chat.title}\n\n» **υηвαη υѕєявσт тєяℓєвιн ∂αнυℓυ ʝιкα ιηgιη мєηggυηαкαη вσт ιηι.**"
            )
            return
    except UserNotParticipant:
        if m.chat.username:
            try:
                await user.join_chat(m.chat.username)
            except Exception as e:
                await m.reply_text(f"❌ **υѕєявσт gαgαℓ вєяgαвυηg**\n\n**reason**:{e}")
                return
        else:
            try:
                pope = await c.export_chat_invite_link(chat_id)
                pepo = await c.revoke_chat_invite_link(chat_id, pope)
                await user.join_chat(pepo.invite_link)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await m.reply_text(
                    f"❌ **υѕєявσт gαgαℓ вєяgαвυηg**\n\n**reason**:{e}"
                )

    if len(m.command) < 2:
        await m.reply("» give me a live-link/m3u8 url/youtube link to stream.")
    else:
        link = m.text.split(None, 1)[1]
        suhu = await m.reply("🔄 **ρяσ¢єѕѕιηg ѕтяєαм...**")

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
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **ℓα¢αк ∂ιтαмвαнкαη кє αηтяєαη**\n\n💭 **¢нαт:** `{chat_id}`\n🎧 **яєqυєѕт вує:** {requester}\n🔢 **αηтяι ∂ι ρσѕιѕι »** `{pos}`",
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
                    requester = (
                        f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                    )
                    await m.reply_photo(
                        photo=f"{IMG_2}",
                        caption=f"💡 **[яα∂ισ ℓινє]({link}) ѕтяєαм ѕтαятє∂.**\n\n💭 **¢нαт:** `{chat_id}`\n💡 **ѕтαтυѕ:** `Playing`\n🎧 **яєqυєѕт вує:** {requester}",
                        reply_markup=keyboard,
                    )
                except Exception as ep:
                    await m.reply_text(f"🚫 error: `{ep}`")
