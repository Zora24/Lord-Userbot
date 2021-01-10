# Copyright (C) 2020 Aidil Aryanto.
# DeeezLoad Ported from UniBorg by AnggaR96s
# All rights reserved.

import asyncio
import glob
import os
import shutil
import time

import deezloader
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pylast import User
from selenium import webdriver
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeAudio, DocumentAttributeVideo

from userbot import (
    CMD_HELP,
    DEEZER_ARL_TOKEN,
    GOOGLE_CHROME_BIN,
    LASTFM_USERNAME,
    TEMP_DOWNLOAD_DIRECTORY,
    bot,
    lastfm,
)
from userbot.events import register
from userbot.utils import progress


async def getmusicvideo(cat):
    video_link = ""
    search = cat
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.youtube.com/results?search_query=" + search)
    user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    for i in user_data:
        video_link = i.get_attribute("href")
        break
    command = 'youtube-dl -f "[filesize<50M]" --merge-output-format mp4 ' + video_link
    os.system(command)


@register(outgoing=True, pattern=r"^\.netease (?:(now)|(.*) - (.*))")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1) == "now":
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        if playing is None:
            return await event.edit("`Error: No current scrobble found.`")
        artist = playing.get_artist()
        song = playing.get_title()
    else:
        artist = event.pattern_match.group(2)
        song = event.pattern_match.group(3)
    track = str(artist) + " - " + str(song)
    chat = "@WooMaiBot"
    link = f"/netease {track}"
    await event.edit("`Searching...`")
    try:
        async with bot.conversation(chat) as conv:
            await asyncio.sleep(2)
            await event.edit("`Processing... Please wait`")
            try:
                msg = await conv.send_message(link)
                response = await conv.get_response()
                respond = await conv.get_response()
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.reply("`Please unblock @WooMaiBot and try again`")
                return
            await event.edit("`Sending Your Music...`")
            await asyncio.sleep(3)
            await bot.send_file(event.chat_id, respond)
        await event.client.delete_messages(
            conv.chat_id, [msg.id, response.id, respond.id]
        )
        await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@WooMaiBot` is not responding or Song not found!.`"
        )


@register(outgoing=True, pattern=r"^\.vsong(?: |$)(.*)")
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("`Mencari Musik Video..`")
    elif reply:
        query = str(reply.message)
        await event.edit("`Mencari Musik Video..`")
    else:
        await event.edit("`Apa yang harus saya cari?`")
        return
    await getmusicvideo(query)
    l = glob.glob(("*.mp4")) + glob.glob(("*.mkv")) + glob.glob(("*.webm"))
    if l:
        await event.edit("`OK, Video Musik di Temukan..`")
    else:
        await event.edit(f"`Maaf Saya Tidak dapat Menemukan` **{query}**")
        return
    try:
        loa = l[0]
        metadata = extractMetadata(createParser(loa))
        duration = 0
        width = 0
        height = 0
        if metadata.has("duration"):
            duration = metadata.get("duration").seconds
        if metadata.has("width"):
            width = metadata.get("width")
        if metadata.has("height"):
            height = metadata.get("height")
        os.system("cp *mp4 thumb.mp4")
        os.system("ffmpeg -i thumb.mp4 -vframes 1 -an -s 480x360 -ss 5 thumb.jpg")
        thumb_image = "thumb.jpg"
        c_time = time.time()
        await event.client.send_file(
            event.chat_id,
            loa,
            force_document=False,
            thumb=thumb_image,
            allow_cache=False,
            caption=query,
            supports_streaming=True,
            reply_to=reply_to_id,
            attributes=[
                DocumentAttributeVideo(
                    duration=duration,
                    w=width,
                    h=height,
                    round_message=False,
                    supports_streaming=True,
                )
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, event, c_time, "[UPLOAD]", loa)
            ),
        )
        await event.edit(f"**{query}** `Uploaded Successfully..!`")
        os.remove(thumb_image)
        os.system("rm *.mkv *.mp4 *.webm")
    except BaseException:
        os.remove(thumb_image)
        os.system("rm *.mkv *.mp4 *.webm")
        return


@register(outgoing=True, pattern=r"^\.smd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@SpotifyMusicDownloaderBot"
    await event.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
        await asyncio.sleep(2)
        await event.edit("`Downloading music taking some times,  Stay Tuned.....`")
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=752979930)
            )
            msg = await bot.send_message(chat, link)
            respond = await response
            res = conv.wait_event(
                events.NewMessage(incoming=True, from_users=752979930)
            )
            r = await res
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.reply(
                "```Please unblock @SpotifyMusicDownloaderBot and try again```"
            )
            return
        await bot.forward_messages(event.chat_id, respond.message)
    await event.client.delete_messages(conv.chat_id, [msg.id, r.id, respond.id])
    await event.delete()


@register(pattern=r"^/deez (.+?|) (FLAC|MP3\_320|MP3\_256|MP3\_128)")
async def _(event):
    if event.fwd_from:
        return

    strings = {
        "name": "DeezLoad",
        "arl_token_cfg_doc": "ARL Token for Deezer",
        "invalid_arl_token": "please set the required variables for this module",
        "wrong_cmd_syntax": "bruh, now i think how far should we go. please terminate my Session ð¥º",
        "server_error": "We're experiencing technical difficulties.",
        "processing": "`Downloading..`",
        "uploading": "`Uploading...`",
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
            for required_track in reqd_albums:
                await event.edit(strings["uploading"])
                await upload_track(required_track, event)
            shutil.rmtree(temp_dl_path)

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
            await upload_track(required_track, event)
            await event.edit(strings["uploading"])
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
            for required_track in reqd_albums:
                await event.edit(strings["uploading"])
                await upload_track(required_track, event)
            shutil.rmtree(temp_dl_path)
            await event.delete()

    else:
        await event.edit(strings["wrong_cmd_syntax"])


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
    c_time = time.time()
    await message.client.send_file(
        message.chat_id,
        track_location,
        caption=caption_rts,
        force_document=force_document,
        supports_streaming=supports_streaming,
        allow_cache=False,
        reply_to=message.message.id,
        attributes=document_attributes,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, message, c_time, "[UPLOAD]")
        ),
    )
    os.remove(track_location)


CMD_HELP.update(
    {
        "getmusic": ">`.netease <Artist - Song Title>`"
        "\nUsage: Download music with @WooMaiBot"
        "\n\n>`.netease now`"
        "\nUsage: Download current LastFM scrobble use `@WooMaiBot`."
        "\n\n>`.vsong` **Artist - Song Title**"
        "\nUsage: Finding and uploading videoclip."
        "\n\n>`.smd <Artist - Song Title>`"
        "\nUsage: Download music from Spotify"
        "\n\n>`.deez <spotify/deezer link> FORMAT`"
        "\nUsage: Download music from deezer."
        "\n*Format : `FLAC`, `MP3_320`, `MP3_256`, `MP3_128`."
    }
)
