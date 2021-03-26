# Copyright (C) 2020 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

from covid import Covid
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.covid (.*)")
async def corona(event):
    await event.edit("`Memproses Informasi....`")
    country = event.pattern_match.group(1)
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️Terkonfirmasi : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️Aktif         : {country_data['active']}`\n"
        output_text += f"`🤕Kritis        : {country_data['critical']}`\n"
        output_text += f"`😟Kematian Baru : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️Meninggal     : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔Kasus Baru    : {country_data['new_cases']}`\n"
        output_text += f"`😇Sembuh        : {country_data['recovered']}`\n"
        output_text += "`📍Total Tes     : N/A`\n\n"
        output_text += f"Data disediakan oleh [Worldometer](https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = "Tidak ada informasi ditemukan untuk Negara ini!"

    await event.edit(f"`Info Virus corona di {country}:`\n\n{output_text}")


@register(outgoing=True, pattern="^.covid$")
async def corona(event):
    await event.edit("`Memproses...`")
    country = "World"
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️Terkonfirmasi : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️Aktif         : {country_data['active']}`\n"
        output_text += f"`🤕Kritis        : {country_data['critical']}`\n"
        output_text += f"`😟Kematian Baru : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️Meninggal     : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔Kasus Baru    : {country_data['new_cases']}`\n"
        output_text += f"`😇Sembuh        : {country_data['recovered']}`\n"
        output_text += "`📍Total Tes     : N/A`\n\n"
        output_text += f"Data disediakan oleh [Worldometer](https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = "Tidak ada informasi ditemukan untuk Negara ini!"

    await event.edit(f"`Info Virus corona di {country}:`\n\n{output_text}")


CMD_HELP.update({"covid": "`.covid` **<negara>**"
                 "\nPenjelasan: Dapatkan informasi tentang data covid-19 di suatu Negara.`\n\n"
                 "`.covid`"
                 "\nPenjelasan: Dapatkan informasi tentang data covid-19 di Seluruh Dunia.\n"})
