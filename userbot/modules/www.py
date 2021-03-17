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


@register(outgoing=True, pattern="^Sping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**🐖 ADA BABI🐖 **")
    await pong.edit("**🐖🐖 ADA BABI 🐖🐖**")
    await pong.edit("**🐖🐖🐖 ADA BABI 🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖 LU BABI 🐖🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖🐖 OINKK 🐖🐖🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖🐖🐖 OINKK 🐖🐖🐖🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖🐖🐖🐖 OINKK 🐖🐖🐖🐖🐖🐖🐖**")
    await pong.edit("**mana Babi nya si tolol**")
    await pong.edit("**Woi Babiiiii Muncul woi**")
    await pong.edit("**Nah ini dia babinya**")
    await pong.edit("**Buruan babi nongol**")
    await pong.edit("`.................🐖`")
    await pong.edit("`................🐖.`")
    await pong.edit("`...............🐖..`")
    await pong.edit("`..............🐖...`")
    await pong.edit("`.............🐖....`")
    await pong.edit("`............🐖.....`")
    await pong.edit("`...........🐖......`")
    await pong.edit("`..........🐖.......`")
    await pong.edit("`.........🐖........`")
    await pong.edit("`........🐖.........`")
    await pong.edit("`.......🐖..........`")
    await pong.edit("`......🐖...........`")
    await pong.edit("`.....🐖............`")
    await pong.edit("`....🐖.............`")
    await pong.edit("`...🐖..............`")
    await pong.edit("`..🐖...............`")
    await pong.edit("`.🐖................`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**🐖NGOK🐖** "
                    f"\n  🐽 `%sms` \n"
                    f"**Ada apa memanggil ku?** "
                    f"\n  ➥ `{ALIVE_NAME}` \n" % (duration))


@register(outgoing=True, pattern="^Lping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`ADA MONYET..............🐒🐒🐒🐒`")
    



    await pong.edit("`HUHU HAHA................🐒🐒🐒🐒`")
    


    await pong.edit("`HUHU HAHA................🐒🐒🐒🐒🐒`")
    


    await pong.edit("`BERUBAH JADI SUNGGOKONG RAJA MONYET🐒🐒`")


    await pong.edit("**AKU ADALAH RAJA MONYET,KALIAN SEMUA ADALAH MONYET**")

    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**🐒!**\n"
                    f"🙈 **NYET:** "
                    f"`%sms` \n"
                    f"🙉 **Waktu:** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^Xping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**S**")
    await pong.edit("**ST**")
    await pong.edit("**STR**")
    await pong.edit("**STRE**")
    await pong.edit("**STRES**")
    await pong.edit("**STRESS**")
    await pong.edit("**STRESS U**")
    await pong.edit("**STRESS US**")
    await pong.edit("**STRESS USE**")
    await pong.edit("**STRESS USER**")
    await pong.edit("**STRESS USERB**")
    await pong.edit("**STRESS USERBO**")
    await pong.edit("**STRESS USERBOT**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**😝 ORGIL!**\n"
                    f"↪️ __Gawaras:__ "
                    f"`%sms` \n"
                    f"↪️ __Stress:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^Ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**P̤̈Ï̤N̤̈G̤̈**")
    await pong.edit("**p̲̅o̲̅n̲̅g̲̅**")
    await pong.edit("**ᎦᎿᖇᏋᎦᎦ**")
    await pong.edit("**UྂSྂEྂRྂBྂOྂTྂ**")
    await pong.edit("**P̥ͦI̥ͦN̥ͦG̥ͦ**")
    await pong.edit("**P̥ͦO̥ͦN̥ͦG̥ͦ**")
    await pong.edit("**P̆ĬN̆Ğ**")
    await pong.edit("**P̆ŎN̆Ğ**")
    await pong.edit("**S͟͟T͟͟R͟͟E͟͟S͟͟S͟͟ U͟͟S͟͟E͟͟R͟͟B͟͟O͟͟T͟͟**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**▩⃟꣄ꪾ❁⃟݄ࣾ݃⊣ ╌╌╌╌╼⃘۪۪❁⃘̸۪۪⃗╾╌╌╌╌╸▩⃟꣄ꪾ❁⃟݄ࣾ݃⊣** \n"
                    f"**        ➪STRESS-Userbot➪** \n"
                    f"**▩⃟꣄ꪾ❁⃟݄ࣾ݃⊣ ╌╌╌╌╼⃘۪۪❁⃘̸۪۪⃗╾╌╌╌╌╸▩⃟꣄ꪾ❁⃟݄ࣾ݃⊣** \n"          
                    f"**♛ Sinyal:** `%sms` \n"
                    f"**♛ Tuanku:** `{ALIVE_NAME}` \n"
                    f"**╼═════════════════╾** \n" % (duration))
                    
@register(outgoing=True, pattern="^Speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("**......................................🏍️**")
    await spd.edit("**.....................................🏍️.**")
    await spd.edit("**....................................🏍️..**")
    await spd.edit("**...................................🏍️...**")
    await spd.edit("**..................................🏍️....**")
    await spd.edit("**.................................🏍️.....**")
    await spd.edit("**................................🏍️......**")
    await spd.edit("**...............................🏍️.......**")
    await spd.edit("**..............................🏍️........**")
    await spd.edit("**.............................🏍️.........**")
    await spd.edit("**............................🏍️..........**")
    await spd.edit("**...........................🏍️...........**")
    await spd.edit("**..........................🏍️............**")
    await spd.edit("**.........................🏍️.............**")
    await spd.edit("**........................🏍️..............**")
    await spd.edit("**.......................🏍️...............**")
    await spd.edit("**......................🏍️................**")
    await spd.edit("**..........👨‍🦯.TIIIIN..🏍️.................**")
    await spd.edit("**.........👨‍🦯MINGGIR..🏍️..................**")
    await spd.edit("**.........👨‍🦯GOBLOK..🏍️...................**")
    await spd.edit("**.......👨‍🦯REM NYA..🏍️....................**")
    await spd.edit("**......👨‍🦯.BLOOONG.🏍️.....................**")
    await spd.edit("**......👨‍🦯.YAUDHLH🏍️......................**")
    await spd.edit("**....👨‍🦯Dasar....🏍️.......................**")
    await spd.edit("**...👨‍🦯🏍️.................................**")
    await spd.edit("**.🏍️ Orang Buta**")
    await spd.edit("**.🏍️.**")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Hasil Tes:\n**"
                   "✺ **Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "✺ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✺ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✺ **Ping:** "
                   f"`{result['ping']}` \n"
                   "✺ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "✺ **BOT:** `STRESS Userbot`")


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


@register(outgoing=True, pattern="^Pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("**P**")
    await pong.edit("**PI**")
    await pong.edit("**PIN**")
    await pong.edit("**PING**")
    await pong.edit("**PING P**")
    await pong.edit("**PING PO**")
    await pong.edit("**PING PON**")
    await pong.edit("**PING PONG**")
    await pong.edit("`....................🏎️`")
    await pong.edit("`...................🏎️.`")
    await pong.edit("`..................🏎️..`")
    await pong.edit("`.................🏎️...`")
    await pong.edit("`................🏎️....`")
    await pong.edit("`...............🏎️.....`")
    await pong.edit("`..............🏎️......`")
    await pong.edit("`.............🏎️.......`")
    await pong.edit("`...........🏎️.........`")
    await pong.edit("`..........🏎️..........`")
    await pong.edit("`.........🏎️...........`")
    await pong.edit("`........🏎️............`")
    await pong.edit("`.......🏎️.............`")
    await pong.edit("`......🏎️..............`")
    await pong.edit("`....🏎️................`")
    await pong.edit("`...🏎️.................`")
    await pong.edit("`..🏎️..................`")
    await pong.edit("`.🏎️...................`")
    await pong.edit("`DUARRRR KONTOLL.....💥🤯💣`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("😡 **STRESS!**\n`%sms`" % (duration))

CMD_HELP.update(
    {"ping": "`Ping` ; `Lping` ; `Xping` ; `Sping`\
    \nUsage: Untuk menunjukkan ping bot.\
    \n\n`Speed`\
    \nUsage: Untuk menunjukkan kecepatan.\
    \n\n`Pong`\
    \nUsage: sama kaya perintah ping."
     })
