# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot module containing commands for interacting with dogbin(https://del.dog)"""

import os
from requests import get, post, exceptions
from userbot import BOTLOG_CHATID, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register

DOGBIN_URL = "https://del.dog/"


@register(outgoing=True, pattern=r"^\.paste(?: |$)([\s\S]*)")
async def paste(pstl):
    """ For .paste command, pastes the text directly to dogbin. """
    dogbin_final_url = ""
    match = pstl.pattern_match.group(1).strip()
    reply_id = pstl.reply_to_msg_id

    if not (match or reply_id):
        return await pstl.edit("`Elon Musk berkata saya tidak bisa menempelkan kekosongan Master....⚡.`")

    if match:
        message = match
    elif reply_id:
        message = await pstl.get_reply_message()
        if message.media:
            downloaded_file_name = await pstl.client.download_media(
                message, TEMP_DOWNLOAD_DIRECTORY,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8")
            os.remove(downloaded_file_name)
        else:
            message = message.message

    # Dogbin
    await pstl.edit("`Menempelkan teks . . .🚀`")
    resp = post(DOGBIN_URL + "documents", data=message.encode("utf-8"))

    if resp.status_code == 200:
        response = resp.json()
        key = response["key"]
        dogbin_final_url = DOGBIN_URL + key

        if response["isUrl"]:
            reply_text = (
                "`Berhasil ditempel!`\n\n"
                f"[Shortened URL]({dogbin_final_url})\n\n"
                "`Original(non-shortened) URLs`\n"
                f"[Dogbin URL]({DOGBIN_URL}v/{key})\n"
                f"[View RAW]({DOGBIN_URL}raw/{key})"
            )
        else:
            reply_text = (
                "`Berhasil ditempel!`\n\n"
                f"[Dogbin URL]({dogbin_final_url})\n"
                f"[View RAW]({DOGBIN_URL}raw/{key})"
            )
    else:
        reply_text = "`Gagal menjangkau Dogbin`"

    await pstl.edit(reply_text)
    if BOTLOG_CHATID:
        await pstl.client.send_message(
            BOTLOG_CHATID, "Kueri tempel berhasil dijalankan",
        )


@register(outgoing=True, pattern=r"^\.getpaste(?: |$)(.*)")
async def get_dogbin_content(dog_url):
    """ For .getpaste command, fetches the content of a dogbin URL. """
    textx = await dog_url.get_reply_message()
    message = dog_url.pattern_match.group(1)
    await dog_url.edit("`Mendapatkan konten dogbin...🚀`")

    if textx:
        message = str(textx.message)

    format_normal = f"{DOGBIN_URL}"
    format_view = f"{DOGBIN_URL}v/"

    if message.startswith(format_view):
        message = message[len(format_view):]
    elif message.startswith(format_normal):
        message = message[len(format_normal):]
    elif message.startswith("del.dog/"):
        message = message[len("del.dog/"):]
    else:
        return await dog_url.edit("`Apakah itu url dogbin?`")

    resp = get(f"{DOGBIN_URL}raw/{message}")

    try:
        resp.raise_for_status()
    except exceptions.HTTPError as HTTPErr:
        await dog_url.edit(
            "Permintaan mengembalikan kode status tidak berhasil.\n\n" + str(HTTPErr)
        )
        return
    except exceptions.Timeout as TimeoutErr:
        await dog_url.edit("Permintaan waktu habis." + str(TimeoutErr))
        return
    except exceptions.TooManyRedirects as RedirectsErr:
        await dog_url.edit(
            "Permintaan melebihi jumlah pengalihan maksimum yang dikonfigurasi."
            + str(RedirectsErr)
        )
        return

    reply_text = (
        "`Berhasil mengambil konten URL dogbin!`"
        "\n\n`Content:` " + resp.text)

    await dog_url.edit(reply_text)
    if BOTLOG_CHATID:
        await dog_url.client.send_message(
            BOTLOG_CHATID, "Kueri konten get dogbin telah berhasil dijalankan",
        )


CMD_HELP.update({
    "dogbin":
    " .paste <text / reply> "
    "\ nPenggunaan: Buat tempel atau url yang dipersingkat menggunakan dogbin (https://del.dog/)"
    "\ n \ n.getpaste <reply / link>"
    "\ nPenggunaan: Mendapat konten tempel atau url yang dipersingkat dari dogbin (https://del.dog/)"
})
