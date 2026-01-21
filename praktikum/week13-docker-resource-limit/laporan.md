
# Laporan Praktikum Minggu [13]
Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : Keysya Ayu Anggita  
- **NIM**   : 250202944  
- **Kelas** : 1 IKRA

---

## Tujuan
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.

---

## Dasar Teori
* **Container Concept**
  
  Container merupakan lingkungan terisolasi yang menjalankan aplikasi dengan berbagi kernel sistem operasi, sehingga akses terhadap resource sistem perlu           dibatasi agar tidak saling mengganggu.

* **CPU Limitation**
  
  Limit CPU diterapkan untuk mencegah satu container menggunakan seluruh waktu prosesor, sehingga pembagian CPU antar aplikasi tetap adil dan sistem berjalan       stabil.

* **Memory Limitation**
  
  Limit memori bertujuan mengontrol penggunaan memori oleh aplikasi agar tidak melebihi kapasitas yang tersedia dan menyebabkan penurunan kinerja sistem.

* **Dampak Tanpa Resource Limit**
  
  Tanpa pembatasan CPU dan memori, container dapat menyebabkan kehabisan resource, menurunkan performa aplikasi lain, dan mengganggu stabilitas sistem.

---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
docker ps
docker build -t week13-resource-limit .
docker run --rm week13-resource-limit
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
docker stats
```
**app.py**
```bash
import time

buffer_memori = []
putaran = 1

print("=== Uji Konsumsi Resource Docker ===")
print("Program berjalan terus, hentikan dengan Ctrl + C\n")

try:
    while True:
        # Beban CPU (operasi aritmatika)
        hasil = sum(i * 2 for i in range(400_000))

        # Beban Memori (±4 MB setiap putaran)
        blok = "A" * 4_000_000
        buffer_memori.append(blok)

        print(
            f"Putaran ke-{putaran} | "
            f"Hasil proses: {hasil} | "
            f"Estimasi penggunaan memori: {putaran * 4} MB"
        )

        putaran += 1
        time.sleep(1)

except MemoryError:
    print("⚠️  Program dihentikan: batas memori container tercapai.")

except KeyboardInterrupt:
    print("\n⛔ Program dihentikan oleh pengguna.")
```

**Dockerfile**
```bash
FROM python:3.10-slim

WORKDIR /usr/src/app

COPY app.py .
ENTRYPOINT ["python", "app.py"]
```
---

## Hasil Eksekusi dan Analisis
**Build Image Docker**
![alt text](<screenshots/build_image.png>)
- Hasil pengujian menunjukkan bahwa proses build Docker image berjalan dengan lancar tanpa error. Dockerfile berhasil dieksekusi menggunakan base image             `python:3.10-slim`, dan file aplikasi dapat disalin dengan baik ke dalam image.

##

**Container Tanpa Limit Resource**
![alt text](<screenshots/tanpa_limit.png>)
- Hasil pengamatan memperlihatkan bahwa container Docker dapat menjalankan program uji resource secara berulang tanpa hambatan. Setiap iterasi menghasilkan nilai   perhitungan CPU yang konsisten, sedangkan konsumsi memori mengalami peningkatan secara bertahap dari nilai rendah hingga melebihi 140 MB. Kondisi ini             menunjukkan bahwa penggunaan CPU dan memori terus bertambah karena container dijalankan tanpa batasan resource.

##

**Container dengan Limit Resource**
![alt text](<screenshots/limit.png>)
- Selanjutnya, container dijalankan dengan pembatasan CPU dan memori menggunakan perintah:
  
  `docker run -it --cpus="0.5" --memory="64m" week13-resource-limit`

  Hasil pengamatan menunjukkan bahwa penerapan pembatasan CPU 0,5 core dan memori 64 MB menyebabkan program tetap berjalan dengan hasil perhitungan yang stabil,    namun kecepatan eksekusi menjadi lebih lambat. Seiring peningkatan penggunaan memori hingga mendekati batas, kinerja program menurun dan berpotensi mengalami     penghentian atau error akibat keterbatasan resource.

##

**Monitoring `docker stats`**

![alt text](<screenshots/docker_stats.png>)

Berikut hasil monitoring `docker stats`:

* Penggunaan CPU pada container **test-mac** sangat rendah, yaitu sekitar 0,01%.
* Konsumsi memori tercatat sebesar 404 KiB dari total 7,67 GiB atau sekitar 0,01%.
* Aktivitas jaringan (NET I/O) hampir tidak ada selama pemantauan.
* Operasi I/O disk (BLOCK I/O) juga tergolong sangat kecil.
* Jumlah proses (PIDS) yang berjalan hanya satu, menunjukkan beban container ringan dan stabil.

---

## Kesimpulan
- Container tanpa pembatasan resource dapat menggunakan CPU dan memori secara bebas. Hal ini membuat program berjalan lebih cepat dan stabil.
- Penerapan limit CPU dan memori menyebabkan kecepatan eksekusi program menurun.
- Hasil monitoring menggunakan docker stats menunjukkan penggunaan resource yang lebih terkontrol pada container dengan limit. Pemantauan ini membantu memahami     kondisi kerja container secara real time.

---

## Quiz
**1. Mengapa container perlu dibatasi CPU dan memori?**

  Container perlu dibatasi CPU dan memori agar satu aplikasi tidak menguasai seluruh resource sistem dan mengganggu aplikasi lain yang berjalan pada host yang      sama. Dalam konsep container, aplikasi dijalankan di atas kernel yang sama dan hanya dibedakan melalui mekanisme pembatasan akses resource. Tanpa pembatasan      CPU dan memori, sebuah container dapat menyebabkan resource starvation, menurunkan performa sistem secara keseluruhan, serta menghilangkan keadilan dalam         pembagian resource antar proses. Container sendiri didefinisikan sebagai lapisan virtual yang membatasi akses proses terhadap resource sistem.

  ##
  
**2. Apa perbedaan VM dan container dalam konteks isolasi resource?**

Virtual Machine (VM) memiliki isolasi resource yang lebih kuat karena setiap VM menjalankan sistem operasi (kernel) sendiri di atas hypervisor, sehingga CPU dan memori benar-benar terpisah antar VM. Sementara itu, container berbagi kernel host, sehingga isolasi resource dilakukan melalui pembatasan akses resource oleh kernel dan bersifat lebih ringan tetapi tidak sekuat VM.

##

**3. Apa dampak limit memori terhadap aplikasi yang boros memori?**

Jika aplikasi menggunakan memori melebihi batas yang ditentukan, kinerja aplikasi akan menurun, aplikasi dapat mengalami kegagalan, atau bahkan dihentikan oleh sistem operasi untuk menjaga stabilitas sistem.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  
  Proses mengunduh dan memasang Docker karena laptop yang digunakan tidak mendukung versi aplikasi terbaru.
  
- Bagaimana cara Anda mengatasinya?
  
  Kendala tersebut diatasi dengan menggunakan versi Docker yang lebih lama agar tetap dapat menjalankan praktikum sesuai kebutuhan.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
