"""
   Heroku manager for your userbot
"""

import codecs
import heroku3
import aiohttp
import math
import os
import requests
import asyncio

from userbot import (
    HEROKU_APP_NAME,
    HEROKU_API_KEY,
    BOTLOG,
    BOTLOG_CHATID,
    CMD_HELP)
from userbot.events import register

heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


"""
   ConfigVars setting, get current var, set var or delete var...
"""


@register(outgoing=True,
          pattern=r"^.(get|del) var(?: |$)(\w*)")
async def variable(var):
    exe = var.pattern_match.group(1)
    if app is None:
        await var.edit("`[HEROKU]"
                       "\nPlease setup your`  **HEROKU_APP_NAME**.")
        return False
    if exe == "get":
        await var.edit("`Getting information...`")
        variable = var.pattern_match.group(2)
        if variable != '':
            if variable in heroku_var:
                if BOTLOG:
                    await var.client.send_message(
                        BOTLOG_CHATID, "#CONFIGVAR\n\n"
                        "**ConfigVar**:\n"
                        f"`{variable}` = `{heroku_var[variable]}`\n"
                    )
                    await var.edit("`Received to BOTLOG_CHATID...`")
                    return True
                else:
                    await var.edit("`Please set BOTLOG to True...`")
                    return False
            else:
                await var.edit("`Information don't exists...`")
                return True
        else:
            configvars = heroku_var.to_dict()
            msg = ''
            if BOTLOG:
                for item in configvars:
                    msg += f"`{item}` = `{configvars[item]}`\n"
                await var.client.send_message(
                    BOTLOG_CHATID, "#CONFIGVARS\n\n"
                    "**ConfigVars**:\n"
                    f"{msg}"
                )
                await var.edit("`Received to BOTLOG_CHATID...`")
                return True
            else:
                await var.edit("`Please set BOTLOG to True...`")
                return False
    elif exe == "del":
        await var.edit("`Deleting information...`")
        variable = var.pattern_match.group(2)
        if variable == '':
            await var.edit("`Specify ConfigVars you want to del...`")
            return False
        if variable in heroku_var:
            if BOTLOG:
                await var.client.send_message(
                    BOTLOG_CHATID, "#DELCONFIGVAR\n\n"
                    "**Delete ConfigVar**:\n"
                    f"`{variable}`"
                )
            await var.edit("`Information deleted...`")
            del heroku_var[variable]
        else:
            await var.edit("`Information don't exists...`")
            return True


@register(outgoing=True, pattern=r'^.set var (\w*) ([\s\S]*)')
async def set_var(var):
    await var.edit("`Setting information...`")
    variable = var.pattern_match.group(1)
    value = var.pattern_match.group(2)
    if variable in heroku_var:
        if BOTLOG:
            await var.client.send_message(
                BOTLOG_CHATID, "#SETCONFIGVAR\n\n"
                "**Change ConfigVar**:\n"
                f"`{variable}` = `{value}`"
            )
        await var.edit("`Information sets...`")
    else:
        if BOTLOG:
            await var.client.send_message(
                BOTLOG_CHATID, "#ADDCONFIGVAR\n\n"
                "**Add ConfigVar**:\n"
                f"`{variable}` = `{value}`"
            )
        await var.edit("`Information added...`")
    heroku_var[variable] = value


"""
    Check account quota, remaining quota, used quota, used app quota
"""


@register(outgoing=True, pattern=r"^.usage(?: |$)")
async def dyno_usage(dyno):
    """
        Get your account Dyno Usage
    """
    await dyno.edit("`Getting Information...`")
    useragent = (
        'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/81.0.4044.117 Mobile Safari/537.36'
    )
    user_id = Heroku.account().id
    headers = {
        'User-Agent': useragent,
        'Authorization': f'Bearer {HEROKU_API_KEY}',
        'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    async with aiohttp.ClientSession() as session:
        async with session.get(heroku_api + path, headers=headers) as r:
            if r.status != 200:
                await dyno.client.send_message(
                    dyno.chat_id,
                    f"`{r.reason}`",
                    reply_to=dyno.id
                )
                await dyno.edit("`Can't get information...`")
                return False
            result = await r.json()
            quota = result['account_quota']
            quota_used = result['quota_used']

            """ - User Quota Limit and Used - """
            remaining_quota = quota - quota_used
            percentage = math.floor(remaining_quota / quota * 100)
            minutes_remaining = remaining_quota / 60
            hours = math.floor(minutes_remaining / 60)
            minutes = math.floor(minutes_remaining % 60)

            """ - User App Used Quota - """
            Apps = result['apps']
            for apps in Apps:
                if apps.get('app_uuid') == app.id:
                    AppQuotaUsed = apps.get('quota_used') / 60
                    AppPercentage = math.floor(
                        apps.get('quota_used') * 100 / quota)
                    break
            else:
                AppQuotaUsed = 0
                AppPercentage = 0

            AppHours = math.floor(AppQuotaUsed / 60)
            AppMinutes = math.floor(AppQuotaUsed % 60)

            await dyno.edit(
                "**Dyno Usage**:\n\n╭━━━━━━━━━━━━━━━━━━━━╮\n"
                f"-> `Penggunaan Dyno `  **{app.name}**:\n"
                f"    •**{AppHours} jam - "
                f"{AppMinutes} menit  -  {AppPercentage}%**"
                "\n ◐━─━─━─━─━──━─━─━─━─━◐\n"
                "-> `Sisa Dyno Bulan Ini`:\n"
                f"    •**{hours} jam - {minutes} menit  "
                f"-  {percentage}%**\n"
                "╰━━━━━━━━━━━━━━━━━━━━╯"
            )
            await asyncio.sleep(20)
            await event.delete()
            return True


@register(outgoing=True, pattern=r"^\.logs")
async def _(dyno):
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply(
            "`Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var.`"
        )
    await dyno.edit("`Getting Logs....`")
    with open("logs.txt", "w") as log:
        log.write(app.get_log())
    fd = codecs.open("logs.txt", "r", encoding="utf-8")
    data = fd.read()
    key = (requests.post("https://nekobin.com/api/documents",
                         json={"content": data}) .json() .get("result") .get("key"))
    url = f"https://nekobin.com/raw/{key}"
    await dyno.edit(f"`Here the heroku logs:`\n\nPasted to: [Nekobin]({url})")
    return os.remove("logs.txt")


CMD_HELP.update({"heroku": ">.`usage`"
                 "\nUsage: Check your heroku dyno hours remaining"
                 "\n\n>`.set var <NEW VAR> <VALUE>`"
                 "\nUsage: add new variable or update existing value variable"
                 "\n!!! WARNING !!!, after setting a variable the bot will restarted"
                 "\n\n>`.get var or .get var <VAR>`"
                 "\nUsage: get your existing varibles, use it only on your private group!"
                 "\nThis returns all of your private information, please be caution..."
                 "\n\n>`.del var <VAR>`"
                 "\nUsage: delete existing variable"
                 "\n!!! WARNING !!!, after deleting variable the bot will restarted"})
