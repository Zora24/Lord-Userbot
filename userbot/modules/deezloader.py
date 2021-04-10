# Copyright (C) 2020 The Authors UniBorg (telegram userbot)
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# requires: deezloader hachoir Pillow
# Ported from UniBorg by AnggaR96s

import os
import shutil
import time

import deezloader
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeAudio

from userbot import CMD_HELP, DEEZER_ARL_TOKEN, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register

# LORD USERBOT
@register(outgoing=True, pattern=r"^\.deez (.+?|) (FLAC|MP3\_320|MP3\_256|MP3\_128)")
async def _(event):
    """DeezLoader by @An0nimia
    Ported for UniBorg by @SpEcHlDe"""
    if event.fwd_from:
        return

    strings = {
        "name": "DeezLoad",
        "arl_token_cfg_doc": "ARL Token untuk Deezer",
        "invalid_arl_token": "tolong setel variabel yang dibutuhkan untuk modul ini",
        "wrong_cmd_syntax": "bruh, sekarang saya pikir seberapa jauh kita harus melangkah. tolong hentikan Sesi saya!",
        "server_error": "Terjadi kesalahan teknis.",
        "processing": "`Sedang Mendownload..`",
        "uploading": "`Sedang Mengunggah...`",
    }

    ARL_TOKEN = DEEZER_ARL_TOKEN

    if ARL_TOKEN is None:
        await event.edit(strings["invalid_arl_token"])
        return

    try:
        loader = deezloader.Login(ARL_TOKEN)
    except Exception as er:
        await event.edit(str(er))
        return

    temp_dl_path = os.path.join(TEMP_DOWNLOAD_DIRECTORY, str(time.time()))
    if not os.path.exists(temp_dl_path):
        os.makedirs(temp_dl_path)

    required_link = event.pattern_match.group(1)
    required_qty = event.pattern_match.group(2)

    await event.edit(strings["processing"])

    if "spotify" in required_link:
        if "track" in required_link:
            required_track = loader.download_trackspo(
                required_link,
                output=temp_dl_path,
                quality=required_qty,
                recursive_quality=True,
                recursive_download=True,
                not_interface=True,
            )
            await event.edit(strings["uploading"])
            await upload_track(required_track, event)
            shutil.rmtree(temp_dl_path)
            await event.delete()

        elif "album" in required_link:
            reqd_albums = loader.download_albumspo(
                required_link,
                output=temp_dl_path,
                quality=required_qty,
                recursive_quality=True,
                recursive_download=True,
                not_interface=True,
                zips=False,
            )
            await event.edit(strings["uploading"])
            for required_track in reqd_albums:
                await upload_track(required_track, event)
            shutil.rmtree(temp_dl_path)
            await event.delete()

    elif "deezer" in required_link:
        if "track" in required_link:
            required_track = loader.download_trackdee(
                required_link,
                output=temp_dl_path,
                quality=required_qty,
                recursive_quality=True,
                recursive_download=True,
                not_interface=True,
            )
            await event.edit(strings["uploading"])
            await upload_track(required_track, event)
            shutil.rmtree(temp_dl_path)
            await event.delete()

        elif "album" in required_link:
            reqd_albums = loader.download_albumdee(
                required_link,
                output=temp_dl_path,
                quality=required_qty,
                recursive_quality=True,
                recursive_download=True,
                not_interface=True,
                zips=False,
            )
            await event.edit(strings["uploading"])
            for required_track in reqd_albums:
                await upload_track(required_track, event)
            shutil.rmtree(temp_dl_path)
            await event.delete()

    else:
        await event.edit(strings["wrong_cmd_syntax"])

# LORD - USERBOT
async def upload_track(track_location, message):
    metadata = extractMetadata(createParser(track_location))
    duration = 0
    title = ""
    performer = ""
    if metadata.has("duration"):
        duration = metadata.get("duration").seconds
    if metadata.has("title"):
        title = metadata.get("title")
    if metadata.has("artist"):
        performer = metadata.get("artist")
    document_attributes = [
        DocumentAttributeAudio(
            duration=duration,
            voice=False,
            title=title,
            performer=performer,
            waveform=None,
        )
    ]
    supports_streaming = True
    force_document = False
    caption_rts = os.path.basename(track_location)
    await message.client.send_file(
        message.chat_id,
        track_location,
        caption=caption_rts,
        force_document=force_document,
        supports_streaming=supports_streaming,
        allow_cache=False,
        attributes=document_attributes,
    )
    os.remove(track_location)

# LORD USERBOT
# @LORDUSERBOT_GROUP
CMD_HELP.update(
    {
        "deezload": "**Modules:** __Deezload__\n\n**Perintah:** `.deez <spotify/deezer link> <Format>`"
        "\n**Penjelasan:** Unduh musik dari deezer."
        "\n\n *Format= `FLAC`, `MP3_320`, `MP3_256`, `MP3_128`."
    }
)
