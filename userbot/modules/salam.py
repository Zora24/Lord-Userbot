from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝘼𝙨𝙨𝙖𝙡𝙖𝙢𝙪𝙖𝙡𝙖𝙞𝙠𝙪𝙢 𝘿𝙪𝙡𝙪 𝘽𝙞𝙖𝙧 𝙎𝙤𝙥𝙖𝙣")


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝘼𝙨𝙨𝙖𝙡𝙖𝙢𝙪𝙖𝙡𝙖𝙞𝙠𝙪𝙢 𝘿𝙪𝙡𝙪 𝘽𝙞𝙖𝙧 𝙎𝙤𝙥𝙖𝙣")


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝙒𝙖𝙖𝙡𝙖𝙞𝙠𝙪𝙢𝙨𝙖𝙡𝙖𝙢")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝙒𝙖𝙖𝙡𝙖𝙞𝙠𝙪𝙢𝙨𝙖𝙡𝙖𝙢")


CMD_HELP.update({
    "salam":
    "`.P`\
\nUsage: Untuk Memberi salam.\
\n\n`.L`\
\nUsage: Untuk Menjawab Salam."
})
