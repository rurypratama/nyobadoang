# Hak Cipta (C) 2020-2021 oleh oke-retard@Github, < https://github.com/okay-retard >.
#
# File ini adalah bagian dari proyek < https://github.com/okay-retard/ZectUserBot >,
# dan dirilis di bawah "Perjanjian Lisensi GNU v3.0".
# Silakan lihat < https://github.com/okay-retard/ZectUserBot/blob/master/LICENSE >
#
# Seluruh hak cipta.

dari config impor PREFIX
impor asyncio
waktu impor
dari datetime impor datetime
dari filter impor pyrogram
dari aplikasi impor Zect, StartTime, CMD_HELP
dari sys impor version_info

dari pyrogram impor __version__ sebagai __pyro_version__
dari pyrogram.types impor Pesan

CMD_HELP.update(
    {
        "Hidup": """
" **Hidup** "
  `alive` -> Pamerkan kepada orang-orang dengan bot Anda menggunakan perintah ini.
  `ping` -> Menampilkan kecepatan respons bot.
"""
    }
)

__utama__ = 0
__kecil__ = 2
__mikro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


def get_readable_time(detik: int) -> str:
    hitung = 0
    ping_waktu = ""
    daftar_waktu = []
    time_suffix_list = ["s", "m", "h", "hari"]

    sementara hitung <4
        hitung += 1
        sisa, hasil = divmod(detik, 60) jika hitung < 3 else divmod(detik, 24)
        jika detik == 0 dan sisa == 0:
            merusak
        time_list.append(int(hasil))
        detik = int(sisa)

    untuk x dalam rentang(len(daftar_waktu)):
        daftar_waktu[x] = str(daftar_waktu[x]) + daftar_akhiran waktu[x]
    if len(daftar_waktu) == 4:
        ping_time += time_list.pop() + ", "

    daftar_waktu.reverse()
    ping_time += ":".join(daftar_waktu)

    kembali ping_time


@app.on_message(filters.command("hidup", PREFIX) & filter.me)
async def hidup(_, m):
    start_time = waktu.waktu()
    uptime = get_readable_time((time.time() - StartTime))
    reply_msg = f"**[Zect](https://github.com/okay-retard/ZectUserBot)**\n"
    reply_msg += f"__Python__: `{__python_version__}`\n"
    reply_msg += f"__@Pyrogram version__: `{__pyro_version__}`\n"
    akhir_waktu = waktu.waktu()
    reply_msg += f"__Aceng uptime__: {uptime}"
    foto = "https://telegra.ph/file/3a3940417afe96110bbb8.jpg"
    tunggu m.delete()
    jika m.reply_to_message:
        tunggu app.send_photo(
            m.chat.id,
            foto,
            keterangan=reply_msg,
            reply_to_message_id=m.reply_to_message.message_id,
        )
    kalau tidak:
        tunggu app.send_photo(m.chat.id, photo, caption=reply_msg)


@app.on_message(filters.command("ping", PREFIX) & filter.me)
async def pingme(_, pesan: Pesan):
    mulai = datetime.now()
    menunggu pesan.edit("`Tod!`")
    akhir = datetime.now()
    m_s = (akhir - mulai). mikrodetik / 1000
    menunggu pesan.edit(f"**Tod!**\n`{m_s} ms`")