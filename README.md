# Bot Sedot Data Situng KPU

**Disclaimer:**

- Aplikasi ini bukan untuk membuktikan hebatnya saya, tapi sebaliknya untuk menunjukkan betapa mudahnya kita sebagai warga negara berkontribusi dengan melakukan monitoring situng KPU dan mendeteksi anomali untuk dilaporkan ke KPU.
- Frekuensi monitoring data bervariasi tergantung dari kecepatan koneksi internet masing-masing.
- Terima kasih pada KPU yang telah melakukan transparansi data sehingga aplikasi ini dapat terwujud

**Seputar Aplikasi**

Aplikasi ini dibuat secara minimalis menggunakan Python3 dan hanya 1 library tambahan yaitu `requests` untuk mengambil data secara langsung dari situs KPU. Data yang didapatkan kemudian dimasukkan ke dalam file CSV dengan penamaan berkas sesuai timestamp.

Semua warga negara Indonesia dipersilahkan untuk mengembangkan lebih lanjut misalkan integrasi dengan database atau pembuatan tampilan yang lebih user friendly.

**Cara Penggunaan**

- Install python 3 terlebih dahulu
- Install library Python Request dengan cara `pip install requests`
- Jalankan melalui terminal / command prompt dengan perintah `python situng.py`
- Biarkan aplikasi berjalan sendiri, nggak perlu ditungguin karena bakal luama banget.
