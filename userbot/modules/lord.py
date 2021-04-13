from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
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
    await typew.edit("**deep gembel☑️**")
    await typew.edit("**deep tolol✅**")
    sleep(2)
    await typew.edit("**tepen haram☑️**")
    await typew.edit("**tepen pecundang✅**")
    sleep(1)
    await typew.edit("**oyee anak kontol☑️**")
    await typew.edit("**oyee kepala botak✅**")
    sleep(1)
    await typew.edit("**Kalian Semua GEMBEL,Kecuali JEJE😋**")


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
