""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.remixhelp$")
async def usit(e):
    await e.edit(
        f"Here's something for {DEFAULTUSER} to use it for help_on_update on **XBot-Remix**:\n"
        "\n[Windows Method](https://telegra.ph/How-to-keep-repo-updated-while-keeping-your-changes-through-windows-cmd-method-04-01)"
        "\n[Termux Method](https://telegra.ph/How-to-keep-XBot-Remix-repo-updated-while-keeping-your-changes-through-Termux--kali-linux-06-02)"
        "\n[Kali Linux Method](https://telegra.ph/How-to-keep-OpenUserBot-repo-updated-while-keeping-your-changes-through-Termux-method-04-01)"
        "\n[Ubuntu Linux Method](https://telegra.ph/How-to-keep-OUB-repo-updated-while-keeping-your-changes-through-Ubuntu-Terminal-method-04-01-2)"
        "\n[Gdrive Tutorial](https://telegra.ph/How-To-Setup-Google-Drive-04-03)"
        "\n[video-tutorial](https://youtu.be/us1O-AnWmHA)")


@register(outgoing=True, pattern="^.remixvar$")
async def var(m):
    await m.edit(
        f"Here's a list of VARS for {DEFAULTUSER} on **XBot-Remix**:\n"
        "\n[HEROKU VARS](https://raw.githubusercontent.com/X-Newbie/XBot-Remix/x-sql-extended/varshelper.txt)")


CMD_HELP.update({
    "remixhelper":
    "`.remixhelp`\
\nUsage: Provide links to update repo guides while you keep your changes on the floor.\
\n`.remixvar`\
\nUsage: Provide vars to cross check for you."
})
