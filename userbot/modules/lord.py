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
    await typew.edit("`Halo`"
                     "`Punten`"
                     "kak Mawar`"
                     "`Cuma`"
                     "`Mau`"
                     "`Memberi tahukan`"
                     "`bahwa`"
                     "Aku Cinta Mawar")


@register(outgoing=True, pattern='^.pantau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Masih Ku Pantau**")


# Create by myself @localheart

CMD_HELP.update({
    "lord":
    "`.lord`\
    \nUsage: alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.pantau`\
    \nUsage: coba aja.\
    \n\n`kosong`\
    \nUsage: tunggu update selanjutnya.\
    \n\n`kosong`\
    \nUsage: tunggu update selanjutnya."
})
