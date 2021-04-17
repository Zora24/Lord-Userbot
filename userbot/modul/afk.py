"" "Modul Userbot yang berisi perintah yang berhubungan dengan afk" ""

dari datetime import datetime
waktu impor
dari pilihan impor acak, randint

dari telethon.events impor StopPropagation
dari telethon.tl.functions.account impor UpdateProfileRequest

dari userbot import (# noqa pylint: disable = unused-import isort: skip
    AFKREASON,
    BOTLOG,
    BOTLOG_CHATID,
    CMD_HELP,
    ALIVE_NAME,
    COUNT_MSG,
    ISAFK,
    PM_AUTO_BAN,
    PENGGUNA,
    PM_AUTO_BAN,
    bot,
)
dari userbot.events import register

# ========================= KONSTAN ======================= =====
AFKSTR = [
    f "** Maaf {ALIVE_NAME} Sedang Depresi! **",
    f "** Maaf {ALIVE_NAME} Sedang Depresi \ n Tunggu Sampai Dia Kembali Online! **",
    f "** LORD {ALIVE_NAME} Sedang Depresi \ n Tunggulah Sampai Online **",
    f "** Maaf {ALIVE_NAME} Sedang Depresi! **",
]


global USER_AFK # pylint: nonaktifkan = E0602
global afk_time # pylint: nonaktifkan = E0602
afk_start global
afk_end global
USER_AFK = {}
afk_time = Tidak ada
afk_start = {}

# ================================================= ================


@register (outgoing = True, pattern = "^. dhlh (?: | $) (. *)", disable_errors = True)
async def set_afk (afk_e):
    "" "Untuk perintah .afk, memungkinkan Anda memberi tahu orang-orang bahwa Anda afk saat mereka mengirimi Anda pesan" ""
    pesan = afk_e.text # pylint: nonaktifkan = E0602
    string = afk_e.pattern_match.group (1)
    ISAFK global
    AFKREASON global
    global USER_AFK # pylint: nonaktifkan = E0602
    global afk_time # pylint: nonaktifkan = E0602
    afk_start global
    afk_end global
    pengguna = menunggu bot.get_me () # pylint: nonaktifkan = E0602
    alasan global
    USER_AFK = {}
    afk_time = Tidak ada
    afk_end = {}
    start_1 = datetime.now ()
    afk_start = start_1.replace (mikrodetik = 0)
    jika string:
        AFKREASON = string
        tunggu afk_e.edit (f "** ✘ SORRY! ** \ n ** Gua Lagi Stress! ** \
        \ n☛ ** Alasan: ** `{string}` ")
    lain:
        tunggu afk_e.edit ("** ✘ SORRY! ** \ n ** Gua Lagi Stress! **")
    jika user.last_name:
        menunggu afk_e.client (UpdateProfileRequest (first_name = user.first_name, last_name = user.last_name + "【STRES】"))
    lain:
        menunggu afk_e.client (UpdateProfileRequest (first_name = user.first_name, last_name = "【STRES】"))
    jika BOTLOG:
        tunggu afk_e.client.send_message (BOTLOG_CHATID, "#SORRY! \ n ** Gua Lagi Stress! **")
    ISAFK = Benar
    afk_time = datetime.now () # pylint: nonaktifkan = E0602
    naikkan StopPropagation


@register (keluar = True)
asinkron def type_afk_is_not_true (notafk):
    "" "Ini menyetel status Anda sebagai tidak afk secara otomatis ketika Anda menulis sesuatu ketika sedang afk" ""
    ISAFK global
    COUNT_MSG global
    PENGGUNA global
    AFKREASON global
    global USER_AFK # pylint: nonaktifkan = E0602
    global afk_time # pylint: nonaktifkan = E0602
    afk_start global
    afk_end global
    pengguna = menunggu bot.get_me () # pylint: nonaktifkan = E0602
    last = user.last_name
    jika terakhir dan terakhir. akhiran dengan ("【STRES】"):
        last1 = terakhir [: - 12]
    lain:
        last1 = ""
    back_alive = datetime.now ()
    afk_end = back_alive.replace (mikrodetik = 0)
    jika ISAFK:
        ISAFK = Salah
        msg = menunggu notafk.respond ("** Lord Telah Kembali! **")
        waktu tidur (3)
        menunggu msg.delete ()
        menunggu notafk.client (UpdateProfileRequest (first_name = user.first_name, last_name = last1))
        jika BOTLOG:
            menunggu notafk.client.send_message (
                BOTLOG_CHATID,
                "Anda Dapatkan" + str (COUNT_MSG) + "Pesan Dari" +
                str (len (USERS)) + "Obrolan Saat Anda AFK",
            )
            untuk saya di PENGGUNA:
                name = menunggu notafk.client.get_entity (i)
                name0 = str (name.first_name)
                menunggu notafk.client.send_message (
                    BOTLOG_CHATID,
                    "[" + name0 + "] (tg: // user? id =" + str (i) + ")" +
                    "Mengirim Mu" + "` "+ str (PENGGUNA [i]) +" Pesan` ",
                )
        COUNT_MSG = 0
        PENGGUNA = {}
        AFKREASON = Tidak ada


@register (masuk = True, disable_edited = True)
async def mention_afk (sebutkan):
    "" "Fungsi ini akan memberi tahu orang yang menyebut Anda bahwa Anda AFK." ""
    COUNT_MSG global
    PENGGUNA global
    ISAFK global
    global USER_AFK # pylint: nonaktifkan = E0602
    global afk_time # pylint: nonaktifkan = E0602
    afk_start global
    afk_end global
    pengguna = menunggu bot.get_me () # pylint: nonaktifkan = E0602
    back_alivee = datetime.now ()
    afk_end = back_alivee.replace (mikrodetik = 0)
    afk_since = "** Terakhir Aktif **"
    jika mention.message.mentioned dan tidak (await mention.get_sender ()). bot:
        jika ISAFK:
            now = datetime.now ()
            datime_since_afk = sekarang - afk_time # pylint: nonaktifkan = E0602
            waktu = float (datime_since_afk.seconds)
            hari = waktu // (24 * 3600)
            waktu = waktu% (24 * 3600)
            jam = waktu // 3600
            waktu% = 3600
            menit = waktu // 60
            waktu% = 60
            detik = waktu
            jika hari == 1:
                afk_since = "** Kemarin **"
            elif hari> 1:
                jika hari> 6:
                    date = sekarang + \
                        datetime.timedelta (
                            hari = -hari, jam = -jam, menit = -menit)
                    afk_since = date.strftime ("% A,% Y% B% m,% H:% I")
                lain:
                    wday = now + datetime.timedelta (hari = -hari)
                    afk_since = wday.strftime ('% A')
            jam elif> 1:
                afk_since = f "` {int (jam)} Jam {int (menit)} Menit` "
            elif menit> 0:
                afk_since = f "` {int (menit)} Menit {int (detik)} Detik` "
            lain:
                afk_since = f "` {int (detik)} Detik` "
            jika mention.sender_id tidak ada di USERS:
                jika AFKREASON:
                    tunggu mention.reply (f "** ✘ RAMA {ALIVE_NAME} Lagi stress ** {afk_since} ** Yang Lalu. ** \
                        \ n☛ ** Alasan: ** `{AFKREASON}` ")
                lain:
                    menunggu mention.reply (str (choice (AFKSTR)))
                USERS.update ({mention.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif mention.sender_id di USERS:
                jika PENGGUNA [mention.sender_id]% randint (2, 4) == 0:
                    jika AFKREASON:
                        tunggu mention.reply (f "** ✘ Lord Masih AFK ** {afk_since} ** Yang Lalu. ** \
                            \ n☛ ** Alasan: ** `{AFKREASON}` ")
                    lain:
                        menunggu mention.reply (str (choice (AFKSTR)))
                    PENGGUNA [mention.sender_id] = PENGGUNA [mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                lain:
                    PENGGUNA [mention.sender_id] = PENGGUNA [mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


@register (masuk = Benar, disable_errors = True)
async def afk_on_pm (pengirim):
    "" "Fungsi yang menginformasikan orang bahwa Anda AFK di PM" ""
    ISAFK global
    PENGGUNA global
    COUNT_MSG global
    COUNT_MSG global
    PENGGUNA global
    ISAFK global
    global USER_AFK # pylint: nonaktifkan = E0602
    global afk_time # pylint: nonaktifkan = E0602
    afk_start global
    afk_end global
    pengguna = menunggu bot.get_me () # pylint: nonaktifkan = E0602
    back_alivee = datetime.now ()
    afk_end = back_alivee.replace (mikrodetik = 0)
    afk_since = "** Belum Lama **"
    jika sender.is_private dan sender.sender_id! = 777000 dan bukan (
            menunggu sender.get_sender ()). bot:
        jika PM_AUTO_BAN:
            mencoba:
                dari userbot.modules.sql_helper.pm_permit_sql impor is_approved
                apprv = is_approved (sender.sender_id)
            kecuali AttributeError:
                apprv = Benar
        lain:
            apprv = Benar
        jika apprv dan ISAFK:
            now = datetime.now ()
            datime_since_afk = sekarang - afk_time # pylint: nonaktifkan = E0602
            waktu = float (datime_since_afk.seconds)
            hari = waktu // (24 * 3600)
            waktu = waktu% (24 * 3600)
            jam = waktu // 3600
            waktu% = 3600
            menit = waktu // 60
            waktu% = 60
            detik = waktu
            jika hari == 1:
                afk_since = "** Kemarin **"
            elif hari> 1:
                jika hari> 6:
                    date = sekarang + \
                        datetime.timedelta (
                            hari = -hari, jam = -jam, menit = -menit)
                    afk_since = date.strftime ("% A,% Y% B% m,% H:% I")
                lain:
                    wday = now + datetime.timedelta (hari = -hari)
                    afk_since = wday.strftime ('% A')
            jam elif> 1:
                afk_since = f "` {int (jam)} Jam {int (menit)} Menit` "
            elif menit> 0:
                afk_since = f "` {int (menit)} Menit {int (detik)} Detik` "
            lain:
                afk_since = f "` {int (detik)} Detik` "
            jika sender.sender_id tidak ada di USERS:
                jika AFKREASON:
                    menunggu sender.reply (f "✘ ** Lord Sedang AFK ** {afk_since} ** Yang Lalu **. \
                        \ n☛ ** Alasan **: `{AFKREASON}` ")
                lain:
                    menunggu pengirim.reply (str (pilihan (AFKSTR)))
                USERS.update ({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv dan sender.sender_id di PENGGUNA:
                jika PENGGUNA [sender.sender_id]% randint (2, 4) == 0:
                    jika AFKREASON:
                        menunggu sender.reply (f "✘ ** Lord Sedang AFK ** {afk_since} ** Yang Lalu. ** \
                            \ n☛ ** Alasan **: `{AFKREASON}` ")
                    lain:
                        menunggu pengirim.reply (str (pilihan (AFKSTR)))
                    PENGGUNA [sender.sender_id] = PENGGUNA [sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                lain:
                    PENGGUNA [sender.sender_id] = PENGGUNA [sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


CMD_HELP.update ({
    "afk":
    "` .afk` [Alasan] \
\ nPenggunaan: Lakukan ketika ingin OFF. \ nSiapapun Yang Balas, Tag, Atau Chat Kamu \
Mereka Akan Tau Alasan Kamu OFF. \ N \ nAFK Bisa Dilakukan Dan Dibatalkan Apapun. \
"
})
