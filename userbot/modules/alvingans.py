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

    animation_interval = 1

    animation_ttl = range(117)

    input_str = event.pattern_match.group(1)

    if input_str == "avengers":

        await event.edit(input_str)

        animation_chars = [
            "Aladdin si om ganteng",
            "Achong si cina sesat",
            "Andre si maska botak",
            "Malika kedelai hitam pilihan",
            "Arjen si kang TMO",
            "Adi si kuli 24jam",
            "Dyka si mata mata",
            "Cece si ratu desah",
            "Steven si ilang ilangan",
            "Reno si caper",
            "Jamrud si brondong sangean",
            "Boy si gondrong ga nyopet",
            "Jo si gembul",
            "Cobor si misterius",
            "Jamal si bocah terbully",
            "Yuhu si bocah lemot",
            "Kimy si cewe caper",
            "Dodo si tukang berak",
            "Anna si TT gede",
            "Cala si mami hot",
            "Coki siapasih",
            "Eja si akang jedag jedug",
            "Saldi si bocah ilang",
            "Gery si cowo cool",
            "Tuni si patkay",
            "Brilian si lelek jawa",
            "Zeen si kembaran dyka",
            "Billa si cewe jutek",
            "Lucifer si cowo beatbox",

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
                     "╬═╬ Hallo Semuanya :) \n"
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
    await typew.edit("`Dadah Semuanya...`          \n　　　　　|"
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
                     "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok..`")


@register(outgoing=True, pattern='^.ular(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("░░░░▓\n"
                     "░░░▓▓\n"
                     "░░█▓▓█\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓███\n"
                     "░░░░██▓▓████\n"
                     "░░░░░██▓▓█████\n"
                     "░░░░░░██▓▓██████\n"
                     "░░░░░░███▓▓███████\n"
                     "░░░░░████▓▓████████\n"
                     "░░░░█████▓▓█████████\n"
                     "░░░█████░░░█████●███\n"
                     "░░████░░░░░░░███████\n"
                     "░░███░░░░░░░░░██████\n"
                     "░░██░░░░░░░░░░░████\n"
                     "░░░░░░░░░░░░░░░░███\n"
                     "░░░░░░░░░░░░░░░░░░░\n")


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


@register(outgoing=True, pattern='^.bernyanyi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Ganteng Doang Gak Bernyanyi (ง˙o˙)ว**")
    sleep(2)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")


@register(outgoing=True, pattern='^.foff(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(".                       /¯ )")
    await typew.edit(".                       /¯ )\n                      /¯  /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")

CMD_HELP.update({
    "vip":
    "`.bulan` ; `.hati` ; `.bernyanyi`\
    \nPenjelasan: liat aja.\
    \n\n`.helikopter` ; `.tank` ; `.tembak`\n`.bundir`\
    \nPenjelasan: liat sendiri\
    \n\n`.y`\
    \nPenjelasan: jempol\
    \n\n`.awkwok`\
    \nPenjelasan: ketawa lari.\
    \n\n`.ular` ; `.babi` ; `.foff` ; `.foto` ; `.ajg`\
    \nPenjelasan: liat sendiri."
})
