from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum ")


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum, Gimana Kabar Kalian?")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumsalam")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumussalam kabar sehat?")


@register(outgoing=True, pattern='^K(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**NGONTOLLLLLL**")


@register(outgoing=True, pattern='^N(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**NGENTOOOOOOOTTTTTTTTTTTT**")

@register(outgoing=True, pattern='^B(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOT DAH LU, GOBLOK!!!!**")


@register(outgoing=True, pattern='^M(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BHAAAKSSSSSSSSS**")

@register(outgoing=True, pattern='^Y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**YAUDAH IYAAAAAA ASU**")

@register(outgoing=True, pattern='^Ms(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EFRY GOBLOKK**")
    sleep(1)
    await typew.edit("**NADIA BUCIN**")
    sleep(1)
    await typew.edit("**TIARA GILA**")
    sleep(1)
    await typew.edit("**ANGGA DEPRESI**")
    sleep(1)
    await typew.edit("**IQBAL NGONTOLL**")
    sleep(1)
    await typew.edit("**RAKA GA KEREN**")
    sleep(1)
    await typew.edit("**ENJELL BAPERAN**")
    sleep(1)
    await typew.edit("**CUMA RAMA YANG KERENN!!!**")
    sleep(1)
    await typew.edit("**KALIAN SEMUA NGONTOLL**")
    sleep(1)
    await typew.edit("**RAMA GANTENG NODEBAT!**")

CMD_HELP.update({
    "salam":
    "`P`\
\nUsage: Untuk Memberi salam.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam.\
\n\n`K`\
\nUsage: Untuk mengontoli mereka.\
\n\n`N`\
\nUsage: Kalo kesel coba aja.\
\n\n`B`\
\nUsage: Buat Ngatain Yang Suka Bacot.\
\n\n`M`\
\nUsage: Tersedak meledek.\
\n\n`Y`\
\nUsage: Buat yang males adu bacot."
})
