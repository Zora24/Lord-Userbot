""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.gabuthelp$")
async def usit(e):
    await e.edit(
        f"**Hai Bos {DEFAULTUSER} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/AkuUserBot)"
        "\n[Repo](https://github.com/Ependelope53/Lord-Userbot)"
        "\n[Instagram](Instagram.com/hendraputraaaaaa)")


@register(outgoing=True, pattern="^.gabutvar$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/Ependelope53/GabutC-UBot/Lord-Userbot/varshelper.txt)")


CMD_HELP.update({
    "gabuthelper":
    "`.gabuthelp`\
\nUsage: Bantuan Untuk GabutC-UBot.\
\n`.gabutvar`\
\nUsage: Melihat Daftar Vars."
})
