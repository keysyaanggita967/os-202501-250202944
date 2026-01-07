
# Laporan Praktikum Minggu [10]
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Keysya Ayu Anggita  
- **NIM**   : 250202944 
- **Kelas** : 1 IKRA 

---

## Tujuan
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah *page fault*.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.
---

## Dasar Teori
Manajemen memori virtual memungkinkan eksekusi proses yang ukurannya lebih besar daripada kapasitas memori fisik (RAM) yang tersedia. Ketika CPU membutuhkan sebuah halaman (page) yang tidak berada di memori utama, maka terjadi page fault. Sistem operasi kemudian harus memuat halaman tersebut dari penyimpanan sekunder (disk) ke memori. Apabila memori sudah penuh, sistem operasi harus menentukan salah satu halaman yang ada di memori untuk digantikan (swap out) menggunakan algoritma page replacement.

FIFO (First-In First-Out) merupakan algoritma page replacement paling sederhana, di mana halaman yang pertama kali masuk ke memori akan menjadi halaman pertama yang diganti ketika terjadi page fault. Algoritma ini biasanya diimplementasikan menggunakan struktur data antrian (queue) atau pointer melingkar untuk melacak halaman yang paling lama berada di memori. Meskipun mudah diterapkan, FIFO tidak mempertimbangkan frekuensi penggunaan halaman sehingga dapat menghasilkan kinerja yang kurang optimal.

LRU (Least Recently Used) adalah algoritma page replacement yang mengganti halaman yang paling lama tidak digunakan. Algoritma ini didasarkan pada asumsi locality of reference, yaitu halaman yang sering digunakan dalam waktu dekat kemungkinan besar akan digunakan kembali. Dengan mempertahankan halaman yang baru saja diakses, LRU umumnya menghasilkan jumlah page fault yang lebih sedikit dibandingkan FIFO, meskipun membutuhkan mekanisme pencatatan akses halaman yang lebih kompleks.


---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan *reference string* berikut sebagai contoh:
   ```
   7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
   ```
   Jumlah frame memori: **3 frame**.

2. **Implementasi FIFO**

   - Simulasikan penggantian halaman menggunakan algoritma FIFO.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

3. **Implementasi LRU**

   - Simulasikan penggantian halaman menggunakan algoritma LRU.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

4. **Eksekusi & Validasi**

   - Jalankan program untuk FIFO dan LRU.
   - Pastikan hasil simulasi logis dan konsisten.
   - Simpan screenshot hasil eksekusi.

5. **Analisis Perbandingan**

   Buat tabel perbandingan seperti berikut:

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | ... | ... |
   | LRU | ... | ... |


   - Jelaskan mengapa jumlah *page fault* bisa berbeda.
   - Analisis algoritma mana yang lebih efisien dan alasannya.

6. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
   git push origin main

---

## Kode / Perintah
``` bash
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames_count = 3


def fifo_table(ref, frames_count):
    frames = []
    faults = 0

    print("\nFIFO PAGE REPLACEMENT")
    print("-" * 35)
    print("| No | Page | Status | Frame Isi |")
    print("-" * 35)

    for i, page in enumerate(ref, 1):
        if page in frames:
            status = "HIT"
        else:
            status = "MISS"
            faults += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

        frame_view = " ".join(map(str, frames))
        frame_view += " -" * (frames_count - len(frames))
        print(f"| {i:<2} | {page:<4} | {status:<6} | {frame_view:<10} |")

    print("-" * 35)
    print(f"Total Page Fault FIFO = {faults}")
    return faults


def lru_table(ref, frames_count):
    frames = []
    history = []
    faults = 0

    print("\nLRU PAGE REPLACEMENT")
    print("-" * 35)
    print("| No | Page | Status | Frame Isi |")
    print("-" * 35)

    for i, page in enumerate(ref, 1):
        if page in frames:
            status = "HIT"
            history.remove(page)
        else:
            status = "MISS"
            faults += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                old = history.pop(0)
                frames.remove(old)
                frames.append(page)

        history.append(page)
        frame_view = " ".join(map(str, frames))
        frame_view += " -" * (frames_count - len(frames))
        print(f"| {i:<2} | {page:<4} | {status:<6} | {frame_view:<10} |")

    print("-" * 35)
    print(f"Total Page Fault LRU = {faults}")
    return faults


fifo_fault = fifo_table(reference_string, frames_count)
lru_fault = lru_table(reference_string, frames_count)

print("\nRINGKASAN HASIL")

print(f"Total Page Fault FIFO : {fifo_fault}")
print(f"Total Page Fault LRU  : {lru_fault}")

if fifo_fault < lru_fault:
    print("Algoritma yang lebih efisien: FIFO")
elif lru_fault < fifo_fault:
    print("Algoritma yang lebih efisien: LRU")
else:
    print("Kedua algoritma memiliki efisiensi yang sama")


```


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![alt text](<screenshots/fifolru.png>)

---

## Analisis
Tabel berikut menyajikan perbandingan jumlah page fault yang dihasilkan oleh algoritma FIFO dan LRU 

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | 10 | Jumlah page fault lebih banyak karena halaman yang pertama masuk akan diganti tanpa mempetimbangkan frekuensi penggunaan |
   | LRU | 9 | Jumlah page fault lebih sedikit karena mengganti halaman yang paling lama tidak digunakan |

---
**Jelaskan mengapa jumlah *page fault* bisa berbeda.**

Perbedaan jumlah page fault antara algoritma FIFO dan LRU terjadi karena cara masing-masing algoritma memilih halaman yang akan diganti berbeda, sehingga dampaknya terhadap eisiensi memori juga berbeda.

1. FIFO
   FIFO mengganti halaman yang paling awal masuk ke memori tanpa mempertimbangkan apakah halaman tersebut masih          sering digunakan. Dari simulasi, terlihat bahwa FIFO beberapa kali mengganti halaman yang sebenarnya masih akan       diakses kembali dalam waktu dekat. Akibatnya, ketika halaman tersebut dibutuhkan lagi, terjadi page fault             tambahan. Inilah yang menyebabkan jumlah page fault FIFO menjadi lebih banyak, yaitu 10 kali.
2. LRU
   LRU mengganti halaman yang paling lama tidak digunakan dengan mempertimbangkan riwayat akses halaman.                 Dengan cara ini, halaman yang masih sering digunakan dapat tetap berada di memori lebih lama. Dari hasil simulasi     terlihat bahwa LRU mampu mengurangi terjadinya halaman yang tidak perlu, sehingga jumlah page fault yang              dihasilkan lebih sedikit, yaitu 8 kali.
   
---

**Analisis algoritma mana yang lebih efisien dan alasannya.**

Algoritma LRU lebih efisien dibandingkan FIFO. Alasan utama LRU lebih efisien karena algoritma ini mempertimbangkan riwayat penggunaan halaman.  LRU mengganti halaman yang sering atau baru saja diakses tetap dipertahankan memori. 

---

## Kesimpulan
- Perbedaan jumlah page fault terjadi karena FIFO dan LRU memiliki cara yang berbeda dalam menentukan halaman yang      diganti.
- FIFO kurang efisien karena hanya berdasarkan urutan masuk halaman, tanpa memperhatikan apakah halaman tersebut        masih sering digunakan.
- Halaman yang sering atau baru saja diakses akan dipertahankan lebih lama di memori oleh LRU.

---

## Quiz
**1. Apa perbedaan utama FIFO dan LRU?**

- FIFO menggganti page yang paling lama masuk ke memori tanpa memperhatikan apakah page tersebut masih sering           digunakan, sehingga sederhana tetapi kurang efisien dan bisa mengalami Belady's Anomaly.
- LRU mengganti page yang paling lama tidak digunakan, sehingga lebih mencerminkan pola akses program dan               menghasilkan performa yang lebih baik, tetapi implementasinya lebih kompleks.

---
**2. Mengapa FIFO dapat menghasilkan *Belady’s Anomaly*?**

  FIFO dapat menghasilkan Belady's Anomaly karena algoritma ini tidak  mempertimbangkan locality of reference dan       hanya mengganti page berdasarkan urutan kedatangan memori. Akibatnya, page yang masih sering digunakan dapat tetap    diganti hanya karena masuk lebih awal, sementara page yang jarang digunakan justru bertahan lebih lama. Ketika        jumlah frame ditambah, urutan penggantian page pada FIFO bisa berubah dengan cara yang tidak efisien, sehingga        himpunan page dalam memori tidak bersifat bertingkat (bukan stack algorithm).  Kondisi ini menyebabkan                penambahan   frame tidak menjamin penurunan jumlah page fault, bahkan dalam beberapa kasus justru meningkat, yang     dikenal sebagai Belady's Anomaly.

---
**3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?**

  LRU menghasilkan page fault lebih sedikit karena mempertahankan page yang sering atau baru digunakan sesuai           locality of reference, sedangkan FIFO dapat mengganti page yang masih sering dipakai sehingga lebih banyak fault. 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
