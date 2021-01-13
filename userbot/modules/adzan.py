import json

import requests

from userbot import CMD_HELP
from userbot.events import register

PLACE = ""


@register(pattern=r"^\.adzan(?: |$)(.*)")
async def get_adzan(adzan):
    if not adzan.pattern_match.group(1):
        LOCATION = PLACE
        if not LOCATION:
            await adzan.edit("`Harap Menentukan Kota Atau Negara.`")
            return
    else:
        LOCATION = adzan.pattern_match.group(1)

    # url = f'http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc'
    url = f"https://api.pray.zone/v2/times/today.json?city={LOCATION}"
    request = requests.get(url)
    if request.status_code == 500:
        return await adzan.edit(f"Tidak Dapat Menemukan Kota `{LOCATION}`")

    parsed = json.loads(request.text)

    city = parsed["Hasil"]["Lokasi"]["Kota"]
    country = parsed["Has"]["Lokasi"]["Negara"]
    timezone = parsed["Hasil"]["Lokasi"]["Zona Waktu"]
    date = parsed["Hasil"]["Tanggal Waktu"][0]["Tanggal"]["gregorian"]

    imsak = parsed["Hasil"]["Tanggal Waktu"][0]["Waktu"]["Imsak"]
    subuh = parsed["Hasil"]["Tanggal Waktu"][0]["Waktu"]["Subuh"]
    zuhur = parsed["Hasil"]["Tanggal Waktu"][0]["Waktu"]["Zuhur"]
    ashar = parsed["Hasil"]["Tanggal Waktu"][0]["Waktu"]["Ashar"]
    maghrib = parsed["Hasil"]["Tanggal Waktu"][0]["Waktu"]["Maghrib"]
    isya = parsed["Hasil"]["Tanggal Waktu"][0]["Waktu"]["Isha"]

    result = (
        f"**Jadwal Sholat**:\n"
        f"📅 `{date} | {timezone}`\n"
        f"🌏 `{city} | {country}`\n\n"
        f"**Imsak :** `{imsak}`\n"
        f"**Subuh :** `{subuh}`\n"
        f"**Zuhur :** `{zuhur}`\n"
        f"**Ashar :** `{ashar}`\n"
        f"**Maghrib :** `{maghrib}`\n"
        f"**Isya :** `{isya}`\n"
    )

    await adzan.edit(result)


CMD_HELP.update({"adzan": "\n\n`>.adzan <kota>`"
                 "\nUsage: Memberikan Informasi Waktu Sholat."})
