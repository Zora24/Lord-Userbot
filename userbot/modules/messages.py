# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

from asyncio import sleep

from telethon.errors import rpcbaseerrors

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.purge$")
async def fastpurger(purg):
    chat = await purg.get_input_chat()
    msgs = []
    itermsg = purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id)
    count = 0

    if purg.reply_to_msg_id is not None:
        async for msg in itermsg:
            msgs.append(msg)
            count += 1
            msgs.append(purg.reply_to_msg_id)
            if len(msgs) == 100:
                await purg.client.delete_messages(chat, msgs)
                msgs = []
    else:
        return await purg.edit("`Balas di Pesan Goblokk!!.`")

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id, f"`Berhasil Menghapus Kenangan!`\
        \nSebanyak: {str(count)} Kenangan😭")
    """
    if BOTLOG:
        await purg.client.send_message(
            BOTLOG_CHATID,
            "Kenangan sebanyak: " + str(count) + " berhasil di bersihkan.")
    """
    await sleep(2)
    await done.delete()


@register(outgoing=True, pattern=r"^\.purgeme")
async def purgeme(delme):
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id, from_user="me"):
        if i > count + 1:
            break
        i += 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "`Menghapus Kenangan!` Sebanyak " + str(count) + " Sukses.",
    )
    """
    if BOTLOG:
        await delme.client.send_message(
            BOTLOG_CHATID,
            "Berhasil menghapus " + str(count) + " kenangan.....")
    """
    await sleep(2)
    i = 1
    await smsg.delete()


@register(outgoing=True, pattern=r"^\.del$")
async def delete_it(delme):
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "Deletion of message was successful")
            """
        except rpcbaseerrors.BadRequestError:
            await delme.edit("Well, I can't delete a message")
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "Well, I can't delete a message")
            """


@register(outgoing=True, pattern=r"^\.edit")
async def editer(edit):
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id("me")
    string = str(message[6:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i += 1
    """
    if BOTLOG:
        await edit.client.send_message(BOTLOG_CHATID,
                                       "Edit query was executed successfully")
   """


@register(outgoing=True, pattern=r"^\.sd")
async def selfdestruct(destroy):
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    """
    if BOTLOG:
        await destroy.client.send_message(BOTLOG_CHATID,
                                          "sd query done successfully")
    """


CMD_HELP.update({"purge": ">`.purge`"
                 "\nUsage: Purges all messages starting from the reply.",
                 "purgeme": ">`.purgeme <x>`"
                 "\nUsage: Deletes x amount of your latest messages.",
                 "del": ">`.del`"
                 "\nUsage: Deletes the message you replied to.",
                 "edit": ">`.edit <newmessage>`"
                 "\nUsage: Replace your last message with <newmessage>.",
                 "sd": ">`.sd <x> <message>`"
                 "\nUsage: Creates a message that selfdestructs in x seconds."
                 "\nKeep the seconds under 100 since it puts your bot to sleep.",
                 })
