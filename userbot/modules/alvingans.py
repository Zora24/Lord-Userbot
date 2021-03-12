# Lord-Userbot
from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(117)

    input_str = event.pattern_match.group(1)

    if input_str == "bulan":

        await event.edit(input_str)

        animation_chars = [
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            f"🌖"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 32])


@register(outgoing=True, pattern='^.helikopter(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("▬▬▬.◙.▬▬▬ \n"
                     "═▂▄▄▓▄▄▂ \n"
                     "◢◤ █▀▀████▄▄▄▄◢◤ \n"
                     "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
                     "◥█████◤ \n"
                     "══╩══╩══ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ Hallo ANAK STRESS :) \n"
                     "╬═╬☻/ \n"
                     "╬═╬/▌ \n"
                     "╬═╬/ \\ \n")


@register(outgoing=True, pattern='^.tembak(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("_/﹋\\_\n"
                     "(҂`_´)\n"
                     "<,︻╦╤─ ҉\n"
                     r"_/﹋\_"
                     "\n**Mau Jadi Pacarku Gak?!**")


@register(outgoing=True, pattern='^.bundir(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`DIDUGA BUNDIR KARNA DI GHOSTING...`          \n　　　　　|"
                     "\n　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　／￣￣＼| \n"
                     "＜ ´･ 　　 |＼ \n"
                     "　|　３　 | 丶＼ \n"
                     "＜ 、･　　|　　＼ \n"
                     "　＼＿＿／∪ _ ∪) \n"
                     "　　　　　 Ｕ Ｕ\n")
                     

@register(outgoing=True, pattern='^.awkwok(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("────██──────▀▀▀██\n"
                     "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
                     "▄▀──█▄▄──────█─█▄▄\n"
                     "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
                     "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok Ada kang ghosting..`")


@register(outgoing=True, pattern='^.ular(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("░░░░▓\n"
    await typew.edit("░░░▓▓\n"
    await typew.edit("░░█▓▓█\n"
    await typew.edit("░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░░░██▓▓██\n"
    await typew.edit("░░░░██▓▓██\n"
    await typew.edit("░░░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit("░░██▓▓██\n"
    await typew.edit"░░░██▓▓███\n"
    await typew.edit("░░░░██▓▓████\n"
    await typew.edit("░░░░░██▓▓█████\n"
    await typew.edit("░░░░░░██▓▓██████\n"
    await typew.edit("░░░░░░███▓▓███████\n"
    await typew.edit("░░░░░████▓▓████████\n"
    await typew.edit("░░░░█████▓▓█████████\n"
    await typew.edit("░░░█████░░░█████●███\n"
    await typew.edit("░░████░░░░░░░███████\n"
    await typew.edit("░░███░░░░░░░░░██████\n"
    await typew.edit("░░██░░░░░░░░░░░████\n"
    await typew.edit("░░░░░░░░░░░░░░░░███\n"
    await typew.edit("░░░░░░░░░░░░░░░░░░░\n")


@register(outgoing=True, pattern='^.y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
                     "██████▄▄█‡‡‡‡‡‡████████▄\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
                     "█████‡‡‡‡‡‡‡██████████\n")


@register(outgoing=True, pattern='^.tank(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
                     "▂▄▅█████████▅▄▃▂…\n"
                     "[███████████████████]\n"
                     "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n")


@register(outgoing=True, pattern='^.babi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("┈┈┏━╮╭━┓┈╭━━━━╮\n"
                     "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
                     "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
                     "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
                     "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
                     "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
                     "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
                     "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")


@register(outgoing=True, pattern='^.ajg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("╥━━━━━━━━╭━━╮━━┳\n"
                     "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
                     "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
                     "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
                     "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
                     "╨━━┗┛┗┛━━┗┛┗┛━━┻\n")


@register(outgoing=True, pattern='^.gbn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MAMPUS GUA GBAN NIH ANJING!!**")
    sleep(2)
    await typew.edit("**SIGOBLOK MEMULAI GBAN**")
    sleep(1)
    await typew.edit("**◼️◼️◼️◼️◼️⬛⬛**")
    sleep(1)
    await typew.edit("**⬛⬛⬛⬛◼️◼️◼️◼️**")
    sleep(1)
    await typew.edit("**LIAT NIH GUA GBAN MAMPUS**")
    sleep(1)
    await typew.edit("**3     2      1 **")
    sleep(1)
    await typew.edit("**〰️1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟**")
    sleep(1)
    await typew.edit("**❌❌❌❌❌❌❌❌❌**")
    sleep(1)
    await typew.edit("**EH TAPI KAN LU BABU SINI**")
    sleep(1)
    await typew.edit("**JANGAN DI GBAN DEH MAYAN BUAT BANSUR**")
    sleep(1)
    await typew.edit("**EH TAPI KALO DI SURUH MALAH NGELAWAN**")
    sleep(1)
    await typew.edit("**DI DIEMIN NGELUNJAK CUIHHHHH**")
    sleep(1)
    await typew.edit("**OAAAASUUUUUUUUUUU SIGOBLOK MENGAKTIFKAN**")
    sleep(1)
    await typew.edit("**SEMUA JURUS YANG KU PUNYA UNTUK GBAN**")
    sleep(1)
    await typew.edit("**LIAT NIH YA GUA GBAN**")
    sleep(1)
    await typew.edit("**TAPI BOONG!!!🤪🤪🤪**")
    sleep(1)
    await typew.edit("**PAL PALE PAL PALE,MUKE LU MIRIP TOKEK**")
    sleep(1)
    await typew.edit("**HAYYYYUUUKKKKK,PAM PIPAM PIPAM PIPAM PAM PIPAM PIPAM**")
CMD_HELP.update({
    "vip":
    "`.bulan` ; `.hati` ; `.bernyanyi`\
    \nUsage: liat aja.\
    \n\n`.helikopter` ; `.tank` ; `.tembak`\n`.bundir`\
    \nUsage: liat sendiri\
    \n\n`.y`\
    \nUsage: jempol\
    \n\n`.awkwok`\
    \nUsage: ketawa lari.\
    \n\n`.ular` ; `.babi` ; `.ajg`\
    \nUsage: liat sendiri."
})
