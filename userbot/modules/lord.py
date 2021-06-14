from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.ayg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`HAYY KAMUU`")
    sleep(2)
    await typew.edit("`GUA CUMAN MAU BILANGG`")
    sleep(1)
    await typew.edit("`GUA SAYANG BANGET AMA LU SUMPAHH`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Aku mau nimbrung**")


@register(outgoing=True, pattern='^.jeje(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**jeje ganteng☑️**")
    await typew.edit("**jeje Ganteng✅**")
    sleep(1)
    await typew.edit("**Lu Semua gembel☑️**")
    await typew.edit("**Lu Semua tolol✅**")
    sleep(2)
    await typew.edit("**Lu semua haram☑️**")
    await typew.edit("**Lu semua pecundang✅**")
    sleep(1)
    await typew.edit("**Lu semua anak kontol☑️**")
    await typew.edit("**Lu semua anak bangsat✅**")
    sleep(1)
    await typew.edit("**Intinya Lu Semua GEMBEL,Kecuali JEJE😋**")


# Create by myself @localheart

CMD_HELP.update({
    "stres":
    "`.gembel`\
    \nUsage: alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.jeje`\
    \nUsage: coba aja.\
    \n\n`kosong`\
    \nUsage: tunggu update selanjutnya.\
    \n\n`kosong`\
    \nUsage: tunggu update selanjutnya."
})
