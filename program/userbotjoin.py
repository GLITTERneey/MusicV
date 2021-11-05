import asyncio
from config import BOT_USERNAME, SUDO_USERS
from driver.decorators import authorized_users_only, sudo_users_only, errors
from driver.filters import command, other_filters
from driver.veez import user as USER
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant


@Client.on_message(
    command(["userbotjoin", f"userbotjoin@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
@errors
async def join_group(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except BaseException:
        await message.reply_text(
            "• **ѕαуα тι∂αк ρυηуα ιzιη:**\n\n» ❌ __Add Users__",
        )
        return

    try:
        user = await USER.get_me()
    except BaseException:
        user.first_name = "music assistant"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"🛑 Flood Wait Error 🛑 \n\n**υѕєявσт тι∂αк ∂ρααт вєяgαвυηg ∂єηgαη gяσυρѕ αη∂α кαяєηα вαηуαкηуα ρєямιηтααη вєяgαвυηg υηтυк υѕєявσт**"
            "\n\n**αтαυ тαмвαнкαη αѕιѕтєη ѕє¢αяα мαηυαℓ кє gяσυρѕ αη∂α ∂αη ¢σвα ℓαgι**",
        )
        return
    await message.reply_text(
        f"✅ **υѕєявσт вєянαѕιℓ мємαѕυкι σвяσℓαη ιηι**",
    )


@Client.on_message(command(["userbotleave",
                            f"leave@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def leave_one(client, message):
    try:
        await USER.send_message(message.chat.id, "✅ υѕєявσт вєянαѕιℓ мєηιηggαℓкαη σηяσℓαη")
        await USER.leave_chat(message.chat.id)
    except BaseException:
        await message.reply_text(
            "❌ **υѕєявσт тι∂αк ∂αραт мєηιηggαℓкαη gяσυρѕ αη∂α, ѕєρєятι мєηυηggυ ѕєѕєσяαηg уαηg тαк кυηʝυηg ∂αтαηg.**\n\n**» αтαυ ѕє¢αяα мαηυαℓ мєηєη∂αηg υѕєявσт ∂αяι gяσυρѕ αη∂α**"
        )

        return


@Client.on_message(command(["leaveall", f"leaveall@{BOT_USERNAME}"]))
@sudo_users_only
async def leave_all(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **υѕєявσт** leaving all chats !")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"υѕєявσт мєηιηggαℓкαη ѕємυα gяσυρѕ...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        except BaseException:
            failed += 1
            await lol.edit(
                f"υѕєявσт кєℓυαя вєgιтυ ѕαʝα...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        await asyncio.sleep(0.7)
    await client.send_message(
        message.chat.id, f"✅ ℓєƒт ƒяσмм: {left} chats.\n❌ Failed in: {failed} chats."
    )
