from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.j(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku jeje`")
    sleep(3)
    await typew.edit("`18 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal serang, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
    sleep(1)
    await typew.edit("`Aku Janji Ga Akan`")
    await typew.edit("`ninggalin kamu serius!!`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Hidup`")
    sleep(1)
    await typew.edit("`Walau tak berguna Awowkkw`")
# Create by myself @localheart
