from cache.admins import admins
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL
from driver.decorators import authorized_users_only
from driver.filters import command, other_filters
from driver.queues import QUEUE, clear_queue
from driver.utils import skip_current_song, skip_item
from driver.veez import call_py
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


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
        "✅ 𝐁𝐨𝐭 **𝐑𝐞𝐥𝐨𝐚𝐝 𝐃𝐞𝐧𝐠𝐚𝐧 𝐁𝐞𝐧𝐞𝐫 !**\n✅ **𝐀𝐝𝐦𝐢𝐧 𝐥𝐢𝐬𝐭** 𝐡𝐚𝐬 𝐛𝐞𝐞𝐧 **𝐮𝐩𝐝𝐚𝐭𝐞𝐝 !**"
    )


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✨𝐆𝐫𝐨𝐮𝐩✨", url=f"https://t.me/{GROUP_SUPPORT}"
                ),
                InlineKeyboardButton(
                    text="🌻𝐂𝐡𝐚𝐧𝐧𝐞𝐥🌻", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("❌ 𝐓𝐢𝐝𝐚𝐤 𝐀𝐝𝐚 𝐘𝐚𝐧𝐠 𝐒𝐞𝐝𝐚𝐧𝐠 𝐃𝐢𝐩𝐮𝐭𝐚𝐫")
        elif op == 1:
            await m.reply("✅ __Queues__ is empty.\n\n• 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐦𝐞𝐧𝐢𝐧𝐠𝐠𝐚𝐥𝐤𝐚𝐧 𝐨𝐛𝐫𝐨𝐥𝐚𝐧 𝐬𝐮𝐚𝐫𝐚")
        else:
            await m.reply_photo(
                photo=f"https://telegra.ph/file/f652fef33e7e39386d31b.jpg",
                caption=f"⏭ **𝐌𝐞𝐥𝐨𝐦𝐩𝐚𝐭𝐢 𝐤𝐞 𝐥𝐚𝐠𝐮 𝐛𝐞𝐫𝐢𝐤𝐮𝐭𝐧𝐲𝐚.**\n\n🏷 **𝐍𝐚𝐦𝐞:** [{op[0]}]({op[1]})\n💭 **𝐂𝐡𝐚𝐭:** `{chat_id}`\n💡 **𝐒𝐭𝐚𝐭𝐮𝐬:** `Playing`\n🎧 **𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐛𝐲𝐞:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **𝐥𝐚𝐠𝐮 𝐝𝐢𝐡𝐚𝐩𝐮𝐬 𝐝𝐚𝐫𝐢 𝐚𝐧𝐭𝐫𝐢𝐚𝐧:**"
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
            await m.reply("✅ **𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠 𝐓𝐞𝐥𝐚𝐡 𝐁𝐞𝐫𝐚𝐤𝐡𝐢𝐫 𝐁𝐲𝐞.**")
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **𝐓𝐢𝐝𝐚𝐤 𝐀𝐝𝐚 𝐃𝐚𝐥𝐚𝐦 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠**")


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
                "⏸ **𝐓𝐫𝐚𝐜𝐤 paused.**\n\n• **𝐔𝐧𝐭𝐮𝐤 𝐌𝐞𝐥𝐚𝐧𝐣𝐮𝐭𝐤𝐚𝐧 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠, 𝐆𝐮𝐧𝐚𝐤𝐚𝐧**\n» /resume 𝐜𝐨𝐦𝐦𝐚𝐧𝐝."
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **𝐓𝐢𝐝𝐚𝐤 𝐀𝐝𝐚 𝐃𝐚𝐥𝐚𝐦 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠**")


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
                "▶️ **𝐓𝐫𝐚𝐜𝐤 resumed.**\n\n• **𝐔𝐧𝐭𝐮𝐤 𝐌𝐞𝐧𝐣𝐞𝐝𝐚 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠, 𝐆𝐮𝐧𝐚𝐤𝐚𝐧 𝐓𝐨𝐦𝐛𝐨𝐥**\n» /pause 𝐜𝐨𝐦𝐦𝐚𝐧𝐝."
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **𝐓𝐢𝐝𝐚𝐤 𝐀𝐝𝐚 𝐃𝐚𝐥𝐚𝐦 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠**")


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    try:
        await call_py.change_volume_call(chat_id, volume=int(range))
        await m.reply(f"✅ **𝐕𝐨𝐥𝐮𝐦𝐞 𝐃𝐢𝐬𝐞𝐭𝐞𝐥 𝐊𝐞𝐞** `{range}`%")
    except Exception as e:
        await m.reply(f"🚫 **error:**\n\n{e}")
