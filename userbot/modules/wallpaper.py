# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the General Public License, Version 3.0;
# you may not use this file except in compliance with the License.
#

import asyncio
import os
from asyncio.exceptions import TimeoutError

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.wall(?: |$)(.*)")
async def _(event):
    try:
        query = event.pattern_match.group(1)
        await event.edit("`Processing..`")
        async with bot.conversation("@XBOTGBOT") as conv:
            try:
                query1 = await conv.send_message(f"/wall {query}")
                asyncio.sleep(3)
                r1 = await conv.get_response()
                r2 = await conv.get_response()
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                return await event.reply("Unblock @XBOTGBOT plox")
            if r1.text.startswith("No"):
                return await event.edit(f"`No result found for` **{query}**")
            else:
                img = await event.client.download_media(r1)
                img2 = await event.client.download_media(r2)
                await event.edit("`Uploading..`")
                p = await event.client.send_file(
                    event.chat_id,
                    img,
                    force_document=False,
                    caption="Preview",
                    reply_to=event.reply_to_msg_id,
                )
                await event.client.send_file(
                    event.chat_id,
                    img2,
                    force_document=True,
                    caption=f"{query}",
                    reply_to=p,
                )
                await event.client.delete_messages(
                    conv.chat_id, [r1.id, r2.id, query1.id]
                )
        await event.delete()
        os.system("rm *.png *.jpg")
    except TimeoutError:
        return await event.edit("`@XBOTGBOT isnt responding..`")


CMD_HELP.update({"wallpaper": ">`.wall <query>`"
                 "\nUsage: search beautiful wallpaper image."})
