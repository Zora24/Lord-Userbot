# CREDITS TEAM DARK COBRA
# PORTED FOR LORD USERBOT BY liualvinas/Alvin


from userbot import *

from pytz import country_names as c_n
from pytz import country_timezones as c_tz
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except BaseException:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Channel/Grup Tidak Valid`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`Ini Adalah Channel/Grup Private Atau Lord Terbanned Disana`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel Atau Supergroup Tidak Ada`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Channel/Grup Tidak Valid`")
            return None
    return chat_info


async def get_tz(con):
    """ Get time zone of the given country. """
    if "(Uk)" in con:
        con = con.replace("Uk", "UK")
    if "(Us)" in con:
        con = con.replace("Us", "US")
    if " Of " in con:
        con = con.replace(" Of ", " of ")
    if "(Western)" in con:
        con = con.replace("(Western)", "(western)")
    if "Minor Outlying Islands" in con:
        con = con.replace("Minor Outlying Islands", "minor outlying islands")
    if "Nl" in con:
        con = con.replace("Nl", "NL")

    for c_code in c_n:
        if con == c_n[c_code]:
            return c_tz[c_code]
    try:
        if c_n[con]:
            return c_tz[con]
    except KeyError:
        return


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name


@register(outgoing=True, pattern="^.culik?*()$")
async def lord(e):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`Memproses....`")
    else:
        rkp = await event.edit("`Memproses....`")
    rk1 = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await rkp.edit("`Maaf Lord, Tidak Bisa Menambahkan Pengguna Disini`")
    s = 0
    f = 0
    error = "None"

    await rkp.edit("**STATUS TERMINAL**\n\n`Mendapatkan Pengguna.......`")
    async for user in event.client.iter_participants(rk1.full_chat.id):
        try:
            if error.startswith("Too"):
                return await rkp.edit(
                    f"**Terminal Selsai Bersama Kesalahan**\n(`Mungkin Terkena Limit Dari telethon Mohon Coba Lagi Nanti`)\n**Kesalahan** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people"
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await rkp.edit(
                f"**Menjalankan Terminal...**\n\n• Menambahkan `{s}` Orang \n• Gagal Menambahkan `{f}` Orang\n\n**× Kesalahan:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await rkp.edit(
        f"**Terminal Selsai** \n\n• Berhasil Menambahkan `{s}` Orang \n• Gagal Menambahkan `{f}` Orang"
    )
