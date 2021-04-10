# Copyright (C) 2020 KenHV
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

from sqlalchemy.exc import IntegrityError

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, disable_edited=True, pattern=r"^\.fban(?: |$)(.*)")
async def fban(event):
    """Bans a user from connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import get_flist
    except IntegrityError:
        return await event.edit("**Berjalan pada mode Non-SQL!**")

    if event.is_reply:
        reply_msg = await event.get_reply_message()
        fban_id = reply_msg.from_id
        reason = event.pattern_match.group(1)
        user_link = f"[{fban_id}](tg://user?id={fban_id})"
    else:
        pattern = str(event.pattern_match.group(1)).split()
        fban_id = pattern[0]
        reason = " ".join(pattern[1:])
        user_link = fban_id

    self_user = await event.client.get_me()

    if fban_id == self_user.id or fban_id == "@" + self_user.username:
        return await event.edit(
            "**Error: Tindakan ini telah dicegah oleh protokol FeRuBoT.**"
        )

    if len((fed_list := get_flist())) == 0:
        return await event.edit("**Anda belum terhubung ke federasi mana pun!**")

    await event.edit(f"**Fbanning** {user_link}...")
    failed = []
    total = int(0)

    for i in fed_list:
        total += 1
        chat = int(i.chat_id)
        try:
            async with bot.conversation(chat) as conv:
                await conv.send_message(f"/fban {user_link} {reason}")
                reply = await conv.get_response()
                await bot.send_read_acknowledge(
                    conv.chat_id, message=reply, clear_mentions=True
                )

                if (
                    ("New FedBan" not in reply.text)
                    and ("Starting a federation ban" not in reply.text)
                    and ("Start a federation ban" not in reply.text)
                    and ("FedBan reason updated" not in reply.text)
                ):
                    failed.append(i.fed_name)
        except BaseException:
            failed.append(i.fed_name)

    reason = reason if reason else "Not specified."

    if failed:
        status = f"Gagal melakukan fban di {len(failed)}/{total} federasi.\n"
        for i in failed:
            status += "• " + i + "\n"
    else:
        status = f"Berhasil Fbanned Pengguna ini di {total} federasi."

    await event.edit(
        f"**Fbanned **{user_link}!\n**Alasan:** {reason}\n**Status:** {status}"
    )


@register(outgoing=True, disable_edited=True, pattern=r"^\.unfban(?: |$)(.*)")
async def unfban(event):
    """Unbans a user from connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import get_flist
    except IntegrityError:
        return await event.edit("**Berjalan pada mode Non-SQL!**")

    if event.is_reply:
        reply_msg = await event.get_reply_message()
        unfban_id = reply_msg.from_id
        reason = event.pattern_match.group(1)
        user_link = f"[{unfban_id}](tg://user?id={unfban_id})"
    else:
        pattern = str(event.pattern_match.group(1)).split()
        unfban_id = pattern[0]
        reason = " ".join(pattern[1:])
        user_link = unfban_id

    self_user = await event.client.get_me()

    if unfban_id == self_user.id or unfban_id == "@" + self_user.username:
        return await event.edit("**Tunggu, itu ilegal**")

    if len((fed_list := get_flist())) == 0:
        return await event.edit("**Anda belum menghubungkan federasi apa pun!**")

    await event.edit(f"**Un-fbanning **{user_link}**...**")
    failed = []
    total = int(0)

    for i in fed_list:
        total += 1
        chat = int(i.chat_id)
        try:
            async with bot.conversation(chat) as conv:
                await conv.send_message(f"/unfban {user_link} {reason}")
                reply = await conv.get_response()
                await bot.send_read_acknowledge(
                    conv.chat_id, message=reply, clear_mentions=True
                )

                if (
                    ("New un-FedBan" not in reply.text)
                    and ("I'll give" not in reply.text)
                    and ("Un-FedBan" not in reply.text)
                ):
                    failed.append(i.fed_name)
        except BaseException:
            failed.append(i.fed_name)

    reason = reason if reason else "Not specified."

    if failed:
        status = f"Gagal membatalkan fban di {len(failed)}/{total} federasi.\n"
        for i in failed:
            status += "• " + i + "\n"
    else:
        status = f"Berhasil Un-fbanned Pengguna ini di {total} federasi."

    reason = reason if reason else "Tidak ditentukan."
    await event.edit(
        f"**Un-fbanned** {user_link}!\n**Alasan:** {reason}\n**Status:** {status}"
    )


@register(outgoing=True, pattern=r"^\.addf *(.*)")
async def addf(event):
    """Adds current chat to connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import add_flist
    except IntegrityError:
        return await event.edit("**Berjalan pada mode Non-SQL!**")

    if not (fed_name := event.pattern_match.group(1)):
        return await event.edit("**Berikan nama untuk terhubung ke grup ini!**")

    try:
        add_flist(event.chat_id, fed_name)
    except IntegrityError:
        return await event.edit(
            "**Grup ini sudah terhubung ke daftar federasi.**"
        )

    await event.edit("**Menambahkan grup ini ke daftar federasi!**")


@register(outgoing=True, pattern=r"^\.delf$")
async def delf(event):
    """Removes current chat from connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import del_flist
    except IntegrityError:
        return await event.edit("**Berjalan pada mode Non-SQL!**")

    del_flist(event.chat_id)
    await event.edit("**Menghapus grup ini dari daftar federasi!**")


@register(outgoing=True, pattern=r"^\.listf$")
async def listf(event):
    """List all connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import get_flist
    except IntegrityError:
        return await event.edit("**Berjalan pada mode Non-SQL!**")

    if len((fed_list := get_flist())) == 0:
        return await event.edit("**Anda belum terhubung ke federasi mana pun!**")

    msg = "**Federasi yang terhubung:**\n\n"

    for i in fed_list:
        msg += "• " + str(i.fed_name) + "\n"

    await event.edit(msg)


@register(outgoing=True, disable_edited=True, pattern=r"^\.clearf$")
async def delf(event):
    """Removes all chats from connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import del_flist_all
    except IntegrityError:
        return await event.edit("**Berjalan pada mode Non-SQL!**")

    del_flist_all()
    await event.edit("**Terputus dari semua federasi yang terhubung!**")


CMD_HELP.update(
    {
        "federasi": ".fban <id/username> <alasan>"
        "\nPenjelasan: Larang pengguna dari federasi yang terhubung."
        "\nAnda dapat membalas ke pengguna yang ingin Anda fban atau secara manual memasukkan username/id."
        "\n\n.unfban <id/username> <alasan>"
        "\nPenjelasan: Sama seperti fban tetapi unbans pengguna"
        "\n\n.addf <nama>"
        "\nPenjelasan: Menambahkan grup saat ini dan menyimpannya sebagai <nama> di federasi terhubung."
        "\nMenambahkan satu grup sudah cukup untuk satu federasi."
        "\n\n.delf"
        "\nPenjelasan: Menghapus grup saat ini dari federasi yang terhubung."
        "\n\n.listf"
        "\nPenjelasan: Mencantumkan semua federasi yang terhubung dengan nama yang ditentukan."
    }
)
