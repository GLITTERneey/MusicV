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
        "✅ вσт **яєℓσα∂ ∂єηgαη вєηєя !**\n✅ **α∂мιη ℓιѕт** нαѕ вєєη **υρ∂αтє !**"
    )


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✨gяσυρѕ✨", url=f"https://t.me/{GROUP_SUPPORT}"
                ),
                InlineKeyboardButton(
                    text="🌻¢нαηηєℓ🌻", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("❌ тι∂αк α∂α уαηg ѕє∂αηg ∂ιρυтαя")
        elif op == 1:
            await m.reply("✅ __Queues__ is empty.\n\n• υѕєявσт мєηιηggαℓкαη σвяσℓαη ѕυαяα")
        else:
            await m.reply_photo(
                photo=f"https://telegra.ph/file/f652fef33e7e39386d31b.jpg",
                caption=f"⏭ **мєℓσмραтι кє ℓαgυ вєяιкυтηуα.**\n\n🏷 **ηαмє:** [{op[0]}]({op[1]})\n💭 **¢нαт:** `{chat_id}`\n💡 **ѕтαтυѕ:** `Playing`\n🎧 **яєqυєѕт вує:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **ℓαgυ ∂ιнαρυѕ ∂αяι αηтяιαη:**"
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
            await m.reply("✅ **ѕтяєαмιηg тєℓαн вєяαкнιя вує.**")
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **тι∂αк α∂α ∂αℓαм ѕтяєαмιηg**")


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
                "⏸ **тяα¢к paused.**\n\n• **υηтυк мєℓαηʝυткαη ѕтяєαмιηg, gυηαкαη**\n» /resume ¢σммαη∂."
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **тι∂αк α∂α ∂αℓαм ѕтяєαмιηg**")


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
                "▶️ **тяα¢к resumed.**\n\n• **υηтυк мєηʝє∂α ѕтяєαмιηg, gυηαкαη тσмвσℓ**\n» /pause ¢σммαη∂."
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **тι∂αк α∂α ∂αℓαм ѕтяєαмιηg**")


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    try:
        await call_py.change_volume_call(chat_id, volume=int(range))
        await m.reply(f"✅ **νσℓυмє ∂ιѕєтєℓ кєє** `{range}`%")
    except Exception as e:
        await m.reply(f"🚫 **error:**\n\n{e}")
