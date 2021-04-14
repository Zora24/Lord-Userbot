from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum Mamank ")


@register(outgoing=True, pattern='^.atg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("ASTAGHFIRULLAH.... GOBLOKKKKK!!!!")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumsalam Mamank ")


@register(outgoing=True, pattern='^.ast(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("ASTAGHFIRULLAH......")


@register(outgoing=True, pattern='^K(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KONTOL SOK KERAS LOE GEMBEL**")


@register(outgoing=True, pattern='^N(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**NAMANYA JUGA GEMBEL CAPER SANA SINI BUAT CARI NAMA**")

@register(outgoing=True, pattern='^B(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOT DAH LU, GEMBEL!!!!**")


@register(outgoing=True, pattern='^M(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MATI AJA LU GEMBEL, GAGUNA LU HIDUP DI BUMI*")

@register(outgoing=True, pattern='^Y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**YAUDAH KALO GITU**")


@register(outgoing=True, pattern='^C(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**CUIHHHH, MAKAN AJA MASIH NGEMIS LOE GEMBEL, JANGAN SOK NINGGI YA KONTOL!!**")


@register(outgoing=True, pattern='^S(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**SOKAP BET LU GEMBEL, KAGA ADA ISTILAH NYA GEMBEL TEMENAN AMA BOS!!**")


@register(outgoing=True, pattern='^V(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MACAM BAGUS AE LU BEGITU GEMBEL, AJAK BAPAK LU SINI RIBUT SAMA GUA!!**")


@register(outgoing=True, pattern='^J(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**JELEK BANGET MUKA GEMBEL LOE, NAJIS ANAK HARAM!!!**")


@register(outgoing=True, pattern='^A(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ANAK HARAM BELAGU BET DAH,LAHIR DARI RAHIM GEMBEL JADI JANGAN SO SO NINGGI KATA KATA LOE😆**")

@register(outgoing=True, pattern='^X(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**DIHHH NAJISS HARAM LOE TOLOL, JANGAN BELAGU DIMARI KAGA KEREN LU BGITU!!!!!!!!!!!**")

@register(outgoing=True, pattern='^Z(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GEMBEL, DI TONGKRONGA JADI BABU, DI TELE SOK JAGOAN...**")

@register(outgoing=True, pattern='^H(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOTAN KUNO, KAGA BAKAL NGENA KE MENTAL GUA, CUIHHHH!!!**")

@register(outgoing=True, pattern='^O(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**JANGAN MAEN BOT MULU, ALAY LU GEMBEL,KESANNYA NORAK, CUIHHHH!!!**")

@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK KEREN LOE BEGITU GEMBEL, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU.Cuihhhhh!!!**")

@register(outgoing=True, pattern='^.gc(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("GC OWNER= [TEKAN](https://t.me/ALGTRR)")

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
\n\n`.gc`\
\nUsage: gapenting."
})
