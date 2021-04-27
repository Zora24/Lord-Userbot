# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
import time


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.fping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit(".AMM USERBOT ")
    await pong.edit(".GINI YA ")
    await pong.edit(".JIKA ")
    await pong.edit(".KAMU ")
    await pong.edit(".MEMPUNYAI ")
    await pong.edit(".MASALAH ")
    await pong.edit(".BERSAMA ORANG ")
    await pong.edit(".PERTAMA DEKATI DIA ")
    await pong.edit(".DAN KATAKAN ")
    await pong.edit(".BY ONE PANTEK!! ")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**𖣘 PING** "
                    f"\n  ➥ `%sms` \n"
                    f"**𖣘 AMM** "
                    f"\n  ➥ `{ALIVE_NAME}` \n" % (duration))


@register(outgoing=True, pattern="^.lping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("👑")
    await pong.edit("__**SAYA**__")
    await pong.edit("__**ADALAH**__")
    await pong.edit("__**AMM-USERBOT**__")
    await pong.edit("__**AMM**__")
    await pong.edit("__**USERBOT**__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**『ᴀᴍᴍ-ᴜsᴇʀʙᴏᴛ』**\n"
                    f"👑 **ᴘɪɴɢ:** "
                    f"`%sms` \n"
                    f"👑 **ᴏɴʟɪɴᴇ:** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.xping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Ping..............`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**⌖ Pong!**\n"
                    f"➠ __Ping:__ "
                    f"`%sms` \n"
                    f"➠ __Uptime:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**PING**")
    await pong.edit("**AMM**")
    await pong.edit("**AMM-USERBOT**")
    await pong.edit("**PANTEK KAU**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**〆 AMM Ping 〆**\n"
                    f"〆 **Ping:** "
                    f"`%sms` \n"
                    f"〆 **Uptime:** "
                    f"`{uptime}` \n"
                    f"**〆 My Name:** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.sinyal$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Mengecek Sinyal...`")
    await pong.edit("**0% LOADING**")
    await pong.edit("**20% LOADING**")
    await pong.edit("**40% LOADING**")
    await pong.edit("**60% LOADING**")
    await pong.edit("**80% LOADING**")
    await pong.edit("**100% LOADING**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"- 𝘼 𝙈 𝙈-\n"
                    f"**• ꜱɪɴʏᴀʟ  :** "
                    f"`%sms` \n"
                    f"**• ᴏɴʟɪɴᴇ  :** "
                    f"`{uptime}` \n"
                    f"**• ɴᴀᴍᴇ  :** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Tinggi...🚀`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Hasil Tes:\n**"
                   "❃ **Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "❃ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "❃ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "❃ **Ping:** "
                   f"`{result['ping']}` \n"
                   "❃ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "❃ **BOT:** `Lord Userbot`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`Pong.....🔨`")
    await pong.edit("`Pong....🔨.`")
    await pong.edit("`Pong...🔨..`")
    await pong.edit("`Pong..🔨...`")
    await pong.edit("`Pong.🔨....`")
    await pong.edit("`Pong🔨.....`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("✘ **Ping!**\n`%sms`" % (duration))

CMD_HELP.update(
    {"ping": "`.ping` ; `.lping` ; `.xping` ; `.fping`\
    \nPenjelasan: Untuk menunjukkan ping bot.\
    \n\n`.speed`\
    \nPenjelasan: Untuk menunjukkan kecepatan.\
    \n\n`.pong`\
    \nPenjelasan: sama kaya perintah ping."
     })
CMD_HELP.update(
    {"sinyal": "**Modules:** `Sinyal`\
    \n\n**• Perintah :** `.sinyal`\
    \n  ➥ **Penjelasan :** __Untuk melihat sinyal bot__"})
