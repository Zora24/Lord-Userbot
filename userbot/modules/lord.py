from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(3)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.lord(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`HALLO LORD AKU ADALAH BOT, DAN AKU AKAN SELALU MEMBANTU MU`")

# Create by myself @localheart

CMD_HELP.update({
    "lord":
    "`.lord`\
\nUsage: Bot\
\n\n`.sadboy`\
\nUsage: hiks"
})
