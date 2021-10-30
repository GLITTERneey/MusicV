# Copyright (C) 2021 By VeezMusicProject

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from driver.filters import command, other_filters
from driver.decorators import sudo_users_only, errors

downloads = os.path.realpath("program/downloads")
raw = os.path.realpath(".")

@Client.on_message(command(["rmd", "clear"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **𝐦𝐞𝐧𝐠𝐡𝐚𝐩𝐮𝐬 𝐬𝐞𝐦𝐮𝐚 𝐟𝐢𝐥𝐞 𝐲𝐚𝐧𝐠 𝐝𝐢𝐮𝐧𝐝𝐮𝐡**")
    else:
        await message.reply_text("❌ **𝐭𝐢𝐝𝐚𝐤 𝐚𝐝𝐚 𝐟𝐢𝐥𝐞 𝐲𝐚𝐧𝐠 𝐝𝐢𝐮𝐧𝐝𝐮𝐡**")

        
@Client.on_message(command(["rmw", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw)
    if ls_dir:
        for file in os.listdir(raw):
            if file.endswith('.raw'):
                os.remove(os.path.join(raw, file))
        await message.reply_text("✅ **𝐦𝐞𝐧𝐠𝐡𝐚𝐩𝐮𝐬 𝐬𝐞𝐦𝐮𝐚 𝐟𝐢𝐥𝐞 𝐦𝐞𝐧𝐭𝐚𝐡**")
    else:
        await message.reply_text("❌ **𝐭𝐢𝐝𝐚𝐤 𝐚𝐝𝐚 𝐟𝐢𝐥𝐞 𝐦𝐞𝐧𝐭𝐚𝐡**")


@Client.on_message(command(["cleanup"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.raw *.jpg")
        await message.reply_text("✅ **𝐝𝐢𝐛𝐞𝐫𝐬𝐢𝐡𝐤𝐚𝐧**")
    else:
        await message.reply_text("✅ **𝐬𝐮𝐝𝐚𝐡 𝐝𝐢𝐛𝐞𝐫𝐬𝐢𝐡𝐤𝐚𝐧**")
