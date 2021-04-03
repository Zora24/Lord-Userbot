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


@register(outgoing=True, pattern='^.atg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("ASTAGHFIRULLAH.... GOBLOKKKKK!!!!")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumsalam")


@register(outgoing=True, pattern='^.ast(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("ASTAGHFIRULLAH......")


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


@register(outgoing=True, pattern='^C(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU HINA, GAUSAH SOK KERAS YA ANJENGG!!**")


@register(outgoing=True, pattern='^S(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SOKAP DEH ANJING!!**")


@register(outgoing=True, pattern='^V(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MACAM BAGUS AE LU BEGITU KONTOL!!**")


@register(outgoing=True, pattern='^J(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**JELEK BANGET LU, NAJIS CUIHHHH!!!**")


@register(outgoing=True, pattern='^A(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**PASANG PP DULU DEK,BIAR ORANG SEGRUP TAU BETAPA HINA NYA MUKA LU😆**")

@register(outgoing=True, pattern='^X(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GC SAMPAH, CUIHHHHH!!!!!!!!!!!**")

@register(outgoing=True, pattern='^Z(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**War War Tai anjing, Ketrigger minta sharelok, Udah di sharelok Ga nyamperin,Keras di sosmed Bhakss...**")

@register(outgoing=True, pattern='^H(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Lawak Mulu ocehan lu,Ga ngena ke mental, CUIHHHH!!!**")

@register(outgoing=True, pattern='^O(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**JANGAN MAEN BOT MULU, ALAY LU NGENTOTT,KESANNYA NORAK, CUIHHHH!!!**")

@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Gak keren lu begitu tolol, kuburan bapak lu gw gali buat dijadiin kolam renang anak paud.Cuihhhhh!!!**")

@register(outgoing=True, pattern='^.gi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("[TEKAN](https://www.instagram.com/ramadh20?r=nametag)")

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
\nUsage: Buat yang males adu bacot.\
\n\n`C`\
\nUsage: Buat menghujat.\
\n\n`S`\
\nUsage: Haha sokap.\
\n\n`V`\
\nUsage: Hujat Orang caper.\
\n\n`J`\
\nUsage: Hujat Jamet.\
\n\n`A`\
\nUsage: Hujat yang gapunya muka.\
\n\n`X`\
\nUsage: Ngatain Grup wkwk.\
\n\n`Z`\
\nUsage: teruntuk petarung.\
\n\n`H`\
\nUsage: Coba dewek ah.\
\n\n`.atg`\
\nUsage: Istighfar 1.\
\n\n`.ast`\
\nUsage: Istighfar 2.\
\n\n`O`\
\nUsage: Ngatain org norak.\
\n\n`G`\
\nUsage: Liat Sendiri.\
\n\n`.gi`\
\nUsage: gapenting."
})
