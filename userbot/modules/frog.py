# Yang Hapus Besok Mati Aminnn
# Port By @Vckyouuu


import random

from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError

from userbot.events import register
from userbot import CMD_HELP, bot

@register(outgoing=True, pattern=r"^\.frog (.*)")
async def honkasays(event):
    wai = await event.edit("`Sedang Memprosess!!!`")
    text = event.pattern_match.group(1)
    if not text:
        return await event.edit("`Beri Aku Bebeberapa Teks, Contoh .prog test`")
    try:
        if not text.endswith("."):
            text = text + "."
        if len(text)<=9:
            results = await bot.inline_query("honka_says_bot", text)
            await results[2].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        elif len(text)>=14:
            results = await bot.inline_query("honka_says_bot", text)
            await results[0].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        else:
            results = await bot.inline_query("honka_says_bot", text)
            await results[1].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        await event.delete()
    except ChatSendInlineForbiddenError:
        await event.edit("`Boss! Saya tidak bisa menggunakan hal-hal sebaris di sini...`")
    except ChatSendStickersForbiddenError:
        await event.edit("Maaf Lord, saya tidak bisa mengirim stiker ke sini !!")


CMD_HELP.update({"frog": "**Modules:** __Frog__\n\n**Perintah:** `.frog <teks>`\
    \n**Penjelasan:** Mengirim sebuah animasi sticker kodok."})
