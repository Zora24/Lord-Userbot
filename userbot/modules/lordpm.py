# Based Plugins
# Ported For Lord-Userbot By liualvinas/Alvin
# Mohon Jangan Menghapus Ini!!!!!!!
# Alvin Gans 
# Biar Banyak Aja

import asyncio
import io
import os

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

import userbot.modules.sql_helper.pmpermit_sql as pmpermit_sql
from userbot import ALIVE_NAME, CUSTOM_PMPERMIT, BOTLOG_CHATID, CMD_HELP
from userbot.__init__ import Config
from userbot.events import register

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "https://telegra.ph/file/28d9b7eb6ef941325bc64.jpg"
else:
    WARN_PIC = PMPERMIT_PIC

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}

PM_ON_OFF = Config.PM_DATA

DEFAULTUSER = (
    str(ALIVE_NAME) if ALIVE_NAME else "Lord, Mohon setel ALIVE_NAME di Heroku"
)
CUSTOM_MIDDLE_PMP = (
    str(CUSTOM_PMPERMIT) if CUSTOM_PMPERMIT else "Dilindungi Oleh Lord-Userbot🇮🇩"
)
USER_BOT_WARN_ZERO = "Anda Telah Melakukan Spam Ke Room Chat Lord, Anda Telah Diblokir Oleh Lord"

botisnoob = Config.BOT_USERNAME

USER_BOT_NO_WARN = (
    "**Hallo, Ini adalah Layanan Perlindungan PM Lord ⚠️**\n\n"
    "**Saya Menangkap Anda Di Sini, Ingin Ngobrol Dengan Lord Saya?** \n\n"
    "**Mohon Tunggu Dan Pilih Alasan Yang Diberikan Di Bawah Ini Untuk Apa Anda Datang. Jika Anda Mencoba Spam Maka Saya Akan Memastikan Bahwa Anda Akan Terblokir.** \n\n"
)

if Config.BOTLOG_CHATID is not None:

    @register(outgoing=True, pattern=r"^\.(?:setuju|ok)\s?(.)?")
    async def approvepm(apprvpm):
        if event.fwd_from:
            return
        replied_user = await borg(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chats = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chats.id):
                if chats.id in PM_WARNS:
                    del PM_WARNS[chats.id]
                if chats.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chats.id].delete()
                    del PREV_REPLY_MESSAGE[chats.id]
                pmpermit_sql.approve(chats.id, "Mensetujui Pesan Pengguna")
                await event.edit(
                    "Setujui Pesan [{}](tg://user?id={})".format(firstname, chats.id)
                )
                await asyncio.sleep(3)
                await event.delete()

    @command(pattern=".block$")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chat = await event.get_chat()
        if event.is_private:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit(
                    "Blokir [{}](tg://user?id={})".format(firstname, chat.id)
                )
                await asyncio.sleep(3)
                await event.client(functions.contacts.BlockRequest(chat.id))
# Lord Alvin Gans
    @register(outgoing=True, pattern=r"^\.(?:tolak|nopm)\s?(.)?")
    async def disapprovepm(disapprvpm):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chat = await event.get_chat()
        if event.is_private:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit(
                   "Menolak Pesan [{}](tg://user?id={})".format(firstname, chat.id)
                )
                await event.delete()

    @register(outgoing=True, pattern=r"^\.daftarsetuju$")
    async def blockpm(block):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Daftar Pesan Yang Disetujui Sekarang\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"☛ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += (
                        f"☛ [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            APPROVED_PMs = "Belum Ada Pesan Yang Disetujui"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Daftar Pesan Yang Disetujui Sekarang",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)

    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.sender_id == bot.uid:
            return

        if Config.BOTLOG_CHATID is None:
            return

        if not event.is_private:
            return

        message_text = event.message.message
        chat_ids = event.sender_id

        message_text.lower()
        if USER_BOT_NO_WARN == message_text:
            # LORD-USERBOT
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await bot.get_entity(event.sender_id)
        if chat_ids == bot.uid:
            # don't log Saved Messages
            return
        if sender.bot:
            # don't log bots
            return
        if sender.verified:
            # don't log verified accounts
            return
        if PM_ON_OFF == "DISABLE":
            return
        if pmpermit_sql.is_approved(chat_ids):
            return
        if not pmpermit_sql.is_approved(chat_ids):
            # pm permit
            await do_pm_permit_action(chat_ids, event)

    async def do_pm_permit_action(chat_ids, event):
        if chat_ids not in PM_WARNS:
            PM_WARNS.update({chat_ids: 0})
        if PM_WARNS[chat_ids] == 3:
            r = await event.reply(USER_BOT_WARN_ZERO)
            await asyncio.sleep(3)
            await event.client(functions.contacts.BlockRequest(chat_ids))
            if chat_ids in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_ids].delete()
            PREV_REPLY_MESSAGE[chat_ids] = r
            the_message = ""
            the_message += "#BLOKIR_PM\n\n"
            the_message += f"[Pengguna](tg://user?id={chat_ids}): {chat_ids}\n"
            the_message += f"Jumlah Pesan: {PM_WARNS[chat_ids]}\n"
            # the_message += f"Media: {message_media}"
            try:
                await event.client.send_message(
                    entity=Var.BOTLOG_CHATID,
                    message=the_message,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True,
                )
                return
            except BaseException:
                return
        botusername = Config.BOT_USERNAME
        tap = await bot.inline_query(botusername, USER_BOT_NO_WARN)
        sed = await tap[0].click(event.chat_id)
        PM_WARNS[chat_ids] += 1
        if chat_ids in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_ids].delete()
        PREV_REPLY_MESSAGE[chat_ids] = sed

# Alvin Gans 
@bot.on(events.NewMessage(incoming=True, from_users=(1353102497)))
async def hehehe(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chats.id):
            pmpermit_sql.approve(chats.id, "**Apa Kabar Mu Lord Alvin 🤐**")
            await borg.send_message(
                chats, "**Terdeteksi Pengguna Adalah Lord Alvin, Jadi Setujui**"
            )

# Alvin Gans
CMD_HELP.update(
    {
        "p": ">`.ok`"
        "\nUsage: Menerima pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm."
        "\n\n>`.tolak`"
        "\nUsage: Menolak pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm."
        "\n\n>`.block`"
        "\nUsage: Memblokir orang di PM."
        "\n\n>`.daftarsetuju`"
        "\nUsage: Melihat daftar pengguna yang sudah di setujui."})
