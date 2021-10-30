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
            "• **𝐬𝐚𝐲𝐚 𝐭𝐢𝐝𝐚𝐤 𝐩𝐮𝐧𝐲𝐚 𝐢𝐳𝐢𝐧:**\n\n» ❌ __Add Users__",
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
            f"🛑 Flood Wait Error 🛑 \n\n**𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐭𝐢𝐝𝐚𝐤 𝐝𝐚𝐩𝐚𝐭 𝐛𝐞𝐫𝐠𝐚𝐛𝐮𝐧𝐠 𝐝𝐞𝐧𝐠𝐚𝐧 𝐠𝐫𝐮𝐩 𝐀𝐧𝐝𝐚 𝐤𝐚𝐫𝐞𝐧𝐚 𝐛𝐚𝐧𝐲𝐚𝐤𝐧𝐲𝐚 𝐩𝐞𝐫𝐦𝐢𝐧𝐭𝐚𝐚𝐧 𝐛𝐞𝐫𝐠𝐚𝐛𝐮𝐧𝐠 𝐮𝐧𝐭𝐮𝐤 𝐮𝐬𝐞𝐫𝐛𝐨𝐭**"
            "\n\n**𝐀𝐭𝐚𝐮 𝐭𝐚𝐦𝐛𝐚𝐡𝐤𝐚𝐧 𝐚𝐬𝐢𝐬𝐭𝐞𝐧 𝐬𝐞𝐜𝐚𝐫𝐚 𝐦𝐚𝐧𝐮𝐚𝐥 𝐤𝐞 𝐆𝐫𝐮𝐩 𝐀𝐧𝐝𝐚 𝐝𝐚𝐧 𝐜𝐨𝐛𝐚 𝐥𝐚𝐠𝐢**",
        )
        return
    await message.reply_text(
        f"✅ **𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐛𝐞𝐫𝐡𝐚𝐬𝐢𝐥 𝐦𝐞𝐦𝐚𝐬𝐮𝐤𝐢 𝐨𝐛𝐫𝐨𝐥𝐚𝐧 𝐢𝐧𝐢**",
    )


@Client.on_message(command(["userbotleave",
                            f"leave@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def leave_one(client, message):
    try:
        await USER.send_message(message.chat.id, "✅ 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐛𝐞𝐫𝐡𝐚𝐬𝐢𝐥 𝐦𝐞𝐧𝐢𝐧𝐠𝐠𝐚𝐥𝐤𝐚𝐧 𝐨𝐛𝐫𝐨𝐥𝐚𝐧")
        await USER.leave_chat(message.chat.id)
    except BaseException:
        await message.reply_text(
            "❌ **𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐭𝐢𝐝𝐚𝐤 𝐝𝐚𝐩𝐚𝐭 𝐦𝐞𝐧𝐢𝐧𝐠𝐠𝐚𝐥𝐤𝐚𝐧 𝐠𝐫𝐮𝐩 𝐀𝐧𝐝𝐚, 𝐦𝐮𝐧𝐠𝐤𝐢𝐧 𝐦𝐞𝐧𝐮𝐧𝐠𝐠𝐮 𝐬𝐞𝐬𝐞𝐨𝐫𝐚𝐧𝐠 𝐲𝐚𝐧𝐠 𝐭𝐚𝐤 𝐤𝐮𝐧𝐣𝐮𝐧𝐠 𝐝𝐚𝐭𝐚𝐧𝐠.**\n\n**» 𝐚𝐭𝐚𝐮 𝐬𝐞𝐜𝐚𝐫𝐚 𝐦𝐚𝐧𝐮𝐚𝐥 𝐦𝐞𝐧𝐞𝐧𝐝𝐚𝐧𝐠 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐝𝐚𝐫𝐢 𝐠𝐫𝐮𝐩 𝐀𝐧𝐝𝐚**"
        )

        return


@Client.on_message(command(["leaveall", f"leaveall@{BOT_USERNAME}"]))
@sudo_users_only
async def leave_all(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **𝐮𝐬𝐞𝐫𝐛𝐨𝐭** leaving all chats !")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐦𝐞𝐧𝐢𝐧𝐠𝐠𝐚𝐥𝐤𝐚𝐧 𝐬𝐞𝐦𝐮𝐚 𝐠𝐫𝐮𝐩...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        except BaseException:
            failed += 1
            await lol.edit(
                f"𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐊𝐞𝐥𝐮𝐚𝐫 𝐁𝐞𝐠𝐢𝐭𝐮 𝐒𝐚𝐣𝐚...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        await asyncio.sleep(0.7)
    await client.send_message(
        message.chat.id, f"✅ 𝐋𝐞𝐟𝐭 𝐟𝐫𝐨𝐦: {left} chats.\n❌ Failed in: {failed} chats."
    )
