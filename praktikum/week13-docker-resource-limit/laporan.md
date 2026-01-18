
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
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

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
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
