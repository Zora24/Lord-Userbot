# LORD - USERBOT PORTED
# BY ALVIN / @LIUALVINAS / ALVIN GANTENG

"""
Created by @Jisan7509
Credit @Infinity20998
Userbot plugin fot CatUserbot
"""

# PORTED BY ALVIN / @LIUALVINAS FOR LORD-USERBOT
# BASED PLUGINS FROM CAT

from time import sleep
import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from platform import uname
from userbot.events import register
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node


@register(outgoing=True, pattern="imposter(|n) (.*)")
async def _(event):
    if event.fwd_from:
        return
    lorduser = platform.uname
    USERNAME = f"tg://user?id={lorduser}"
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    text1 = await event.edit("Uhmm... Ada yang salah disini!")
    sleep(2)
    await text1.delete()
    stcr1 = await event.client.send_file(
        event.chat_id, "CAADAQADRwADnjOcH98isYD5RJTwAg"
    )
    text2 = await event.reply(
        f"**[{DEFAULTUSER}]({USERNAME}) :** Saya harus memanggil untuk Berdiskusi"
    )
    sleep(3)
    await stcr1.delete()
    await text2.delete()
    stcr2 = await event.client.send_file(
        event.chat_id, "CAADAQADRgADnjOcH9odHIXtfgmvAg"
    )
    text3 = await event.reply(
        f"**[{DEFAULTUSER}]({USERNAME}) :** Kami harus mengeluarkan si Imposter atau akan kalah "
    )
    sleep(3)
    await stcr2.delete()
    await text3.delete()
    stcr3 = await event.client.send_file(
        event.chat_id, "CAADAQADOwADnjOcH77v3Ap51R7gAg"
    )
    text4 = await event.reply(f"**Orang Lain :** Dimana Dia?? ")
    sleep(2)
    await text4.edit(f"**Orang Lain :** Siapa!?? ")
    sleep(2)
    await text4.edit(
        f"**[{DEFAULTUSER}]({USERNAME}) :** Dia adalah {name}, Aku Melihat {name} Menggunakan Vent,"
    )
    sleep(3)
    await text4.edit(f"**Orang Lain :**Baiklah... Vote {name} ")
    sleep(2)
    await stcr3.delete()
    await text4.delete()
    stcr4 = await event.client.send_file(
        event.chat_id, "CAADAQADLwADnjOcH-wxu-ehy6NRAg"
    )
    lord = await event.reply(f"{name} Dikeluarkan.......")
    sleep(2)
    await lord.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    sleep(0.5)
    await lord.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    sleep(0.5)
    await lord.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    sleep(0.5)
    await lord.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    sleep(0.5)
    await lord.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    sleep(0.5)
    await lord.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    sleep(0.5)
    await lord.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    sleep(0.5)
    await lord.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    sleep(0.5)
    await lord.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    sleep(0.5)
    await lord.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    sleep(0.2)
    await stcr4.delete()
    if cmd == "":
        await lord.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ{name} was an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         0 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
        sleep(4)
        await lord.delete()
        await event.client.send_file(event.chat_id, "CAADAQADLQADnjOcH39IqwyR6Q_0Ag")
    elif cmd == "n":
        await lord.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ{name} was not an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         1 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
        sleep(4)
        await lord.delete()
        await event.client.send_file(event.chat_id, "CAADAQADQAADnjOcH-WOkB8DEctJAg")

# Alvin Gans
# Ported By Alvin / @LiuAlvinas
# Dont Remove This Bgst


@register(outgoing=True, pattern="timp(|n) (.*)")
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    lord = await event.edit(f"{name} Dikeluarkan.......")
    sleep(2)
    await lord.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    sleep(0.8)
    await lord.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    sleep(0.8)
    await lord.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    sleep(0.8)
    await lord.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    sleep(0.8)
    await lord.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    sleep(0.8)
    await lord.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    sleep(0.8)
    await lord.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    sleep(0.8)
    await lord.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    sleep(0.8)
    await lord.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    sleep(0.8)
    await lord.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    sleep(0.2)
    if cmd == "":
        await lord.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ {name} was an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         0 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
    elif cmd == "n":
        await lord.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ {name} was not an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         1 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )

# Ported By Alvin Ganteng

CMD_HELP.update({"imposter": "**Modules :** `Imposter`\
\n\n**Perintah : **`.imposter` / `.impostern` <text>\
\n**Penjelasan : ** Menemukan imposter dengan sticker.\
\n\n**Perintah : **`.timp` / `.timpn` <text>\
\n**Penjelasan : ** Menemukan imposter dengan teks."})
