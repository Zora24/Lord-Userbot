# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
""" Userbot module containing commands for keeping global notes. """

from userbot.events import register
from userbot import CMD_HELP, BOTLOG_CHATID


@register(outgoing=True,
          pattern=r"\$\w*",
          ignore_unsafe=True,
          disable_errors=True)
async def on_snip(event):
    """ Snips logic. """
    try:
        from userbot.modules.sql_helper.snips_sql import get_snip
    except AttributeError:
        return
    name = event.text[1:]
    snip = get_snip(name)
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    if snip and snip.f_mesg_id:
        msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                ids=int(snip.f_mesg_id))
        await event.client.send_message(event.chat_id,
                                        msg_o.message,
                                        reply_to=message_id_to_reply,
                                        file=msg_o.media)
        await event.delete()
    elif snip and snip.reply:
        await event.client.send_message(event.chat_id,
                                        snip.reply,
                                        reply_to=message_id_to_reply)
        await event.delete()


@register(outgoing=True, pattern=r"^.snip (\w*)")
async def on_snip_save(event):
    """ Untuk perintah .snip, simpan snips untuk digunakan di masa mendatang. """
    try:
        from userbot.modules.sql_helper.snips_sql import add_snip
    except AtrributeError:
        await event.edit("`Berjalan pada mode Non-SQL!`")
        return
    keyword = event.pattern_match.group(1)
    string = event.text.partition(keyword)[2]
    msg = await event.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"#SNIP\
            \nKEYWORD: {keyword}\
            \n\nPesan berikut disimpan sebagai data untuk snip, tolong JANGAN menghapusnya !!"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            await event.edit(
                "`Untuk menyimpan potongan dengan media, BOTLOG_CHATID harus disetel.`"
            )
            return
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = "`Berhasil memotong {}. Gunakan` **${}** `di mana saja untuk mendapatkannya`"
    if add_snip(keyword, string, msg_id) is False:
        await event.edit(success.format('updated', keyword))
    else:
        await event.edit(success.format('saved', keyword))


@register(outgoing=True, pattern="^.snips$")
async def on_snip_list(event):
    """ Untuk perintah .snips, daftar snips yang disimpan oleh Anda. """
    try:
        from userbot.modules.sql_helper.snips_sql import get_snips
    except AttributeError:
        await event.edit("`Berjalan pada mode Non-SQL!`")
        return

    message = "`Tidak ada snips yang tersedia saat ini.`"
    all_snips = get_snips()
    for a_snip in all_snips:
        if message == "`No snips available right now.`":
            message = "Available snips:\n"
            message += f"`${a_snip.snip}`\n"
        else:
            message += f"`${a_snip.snip}`\n"

    await event.edit(message)


@register(outgoing=True, pattern=r"^.remsnip (\w*)")
async def on_snip_delete(event):
    """ For .remsnip command, deletes a snip. """
    try:
        from userbot.modules.sql_helper.snips_sql import remove_snip
    except AttributeError:
        await event.edit("`Berjalan pada mode Non-SQL`")
        return
    name = event.pattern_match.group(1)
    if remove_snip(name) is True:
        await event.edit(f"`Berhasil dihapus snip:` **{name}**")
    else:
        await event.edit(f"`Tidak dapat menemukan snip:` **{name}**")


CMD_HELP.update({
    "snips":
    "\
$<snip_name>\
\nUsage: Mendapatkan snip yang ditentukan, di mana saja.\
\n\n`.snip` <name> <data> atau membalas pesan dengan .snip <name>\
\nUsage: Menyimpan pesan sebagai snip (catatan global) dengan nama. (Bekerja dengan foto, dokumen, dan stiker juga!)\
\n\n`.snips`\
\nUsage: Mendapat semua potongan yang disimpan.\
\n\n`.remsnip` <snip_name>\
\nUsage: Menghapus snip yang ditentukan.\
"
})
