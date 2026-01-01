
# Laporan Praktikum Minggu [9]
Topik: Simulasi Algoritma Penjadwalan CPU (FCFS)

---

## Identitas
- **Nama**  : Keysya Ayu Anggita  
- **NIM**   : 250202944
- **Kelas** : 1 IKRA

---

## Tujuan
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
Penjadwalan CPU merupakan bagian dari sistem operasi yang mengatur urutan eksekusi proses agar penggunaan CPU dapat berjalan secara efisien. Karena CPU memiliki keterbatasan dalam mengeksekusi banyak proses secara bersamaan, diperlukan algoritma penjadwalan untuk memastikan setiap proses memperoleh giliran secara teratur.

Algoritma penjadwalan CPU berfungsi menentukan proses yang akan dijalankan terlebih dahulu berdasarkan aturan tertentu. Beberapa algoritma yang sering digunakan meliputi:
- First Come First Served (FCFS), proses dijalankan sesuai urutan          kedatangan.
- Shortest Job First (SJF), proses dengan waktu eksekusi terpendek         diprioritaskan.
- Priority Scheduling, proses dengan prioritas lebih tinggi dijalankan     lebih dulu.
- Round Robin, setiap proses mendapat jatah waktu yang sama.

Simulasi algoritma penjadwalan CPU bertujuan untuk menggambarkan dan menilai kinerja algoritma penjadwalan sebelum diterapkan pada sistem nyata. Simulasi ini memungkinkan pemahaman cara kerja setiap algoritma, perhitungan **waktu tunggu (waiting time)**, **waktu penyelesaian (turnaround time)**, serta evaluasi efisiensi CPU dalam mengeksekusi proses.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```

---

## Kode / Perintah
Berikut adalah potongan kode program yang digunakan untuk mengimplementasikan simulasi algoritma penjadwalan CPU FCFS:
```python
process = ["P1", "P2", "P3", "P4"]
arrival_time = [0, 1, 2, 3]
burst_time = [6, 8, 7, 3]

n = len(process)

start_time = [0] * n
finish_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

# Perhitungan proses pertama
start_time[0] = arrival_time[0]
finish_time[0] = start_time[0] + burst_time[0]
turnaround_time[0] = finish_time[0] - arrival_time[0]
waiting_time[0] = turnaround_time[0] - burst_time[0]

# Proses berikutnya (FCFS)
for i in range(1, n):
    start_time[i] = max(finish_time[i - 1], arrival_time[i])
    finish_time[i] = start_time[i] + burst_time[i]
    turnaround_time[i] = finish_time[i] - arrival_time[i]
    waiting_time[i] = turnaround_time[i] - burst_time[i]

# Menghitung rata-rata TAT dan WT
print(f"| {'AVERAGE':<7} | {'-':<12} | {'-':<10} | {'-':<10} | {'-':<11} | {sum(turnaround_time)/n:<16.2f} | {sum(waiting_time)/n:<12.2f} |")
garis()
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![alt text](<screenshots/hasil_simulasi_week9.png>)

---

## Analisis
**Berikut adalah penjelasan alur kerja program.**

Program simulasi FCFS dimulai dengan memasukkan data proses yang meliputi *process*, *arrival time*, dan *burst time* untuk menggambarkan waktu kedatangan serta durasi eksekusi setiap proses. Setelah itu, program menyiapkan variabel untuk menyimpan nilai *start time*, *finish time*, *turnaround time*, dan *waiting time*. Proses pertama dijalankan segera saat tiba sehingga waktu mulai sama dengan waktu kedatangannya, kemudian waktu selesai dihitung berdasarkan lama eksekusi. Pada proses-proses berikutnya, algoritma First Come First Served diterapkan dengan menentukan waktu mulai sebagai nilai terbesar antara waktu selesai proses sebelumnya dan waktu kedatangan proses yang sedang dijadwalkan, lalu menghitung waktu selesai, waktu putar, dan waktu tunggu sesuai rumus yang digunakan. Seluruh hasil perhitungan selanjutnya disajikan dalam bentuk tabel bergaris agar mudah dianalisis, dan pada bagian akhir program ditampilkan nilai rata-rata turnaround time dan waiting time sebagai ukuran kinerja penjadwalan FCFS.

---
**Bandingkan hasil simulasi dengan perhitungan manual.**

  ![alt text](<screenshots/hasil_simulasi_week9.png>)
  ![alt text](<screenshots/simulasi_manual.png>)

Hasil simulasi algoritma FCFS menunjukkan nilai rata-rata *waiting time* sebesar 8.75 dan *turnaround time* sebesar 14.75, yang konsisten dengan hasil perhitungan manual pada modul praktikum minggu ke-5. Kesamaan hasil ini dapat dilihat dari hasil keduanya yang menunjukkan nilai *waiting time* dan *turnaround time* yang sama. Hal tersebut membuktikan bahwa logika algoritma yang digunakan, seperti pengurutan proses berdasarkan *arrival time* serta perhitungan waktu secara berurutan, telah diterapkan dengan benar dalam kode program. Simulasi yang dijalankan mampu menghasilkan perhitungan yang sama dengan metode manual, namun dengan proses yang lebih cepat, hasil yang konsisten, serta risiko kesalahan yang lebih kecil dibandingkan perhitungan manual yang dilakukan secara bertahap.

---   
**Kelebihan dan keterbatasan simulasi.**
**Kelebihan:**
- Mempermudah perhitungan *start time*, *finish time*, *turnaround         time*, dan *waiting time* secara otomatis
- Mengurangi kemungkinan kesalahan yang sering terjadi pada perhitungan    manual
- Mudah dimodifikasi untuk menguji berbagai dataset proses yang berbeda

**Keterbatasan:**
- Tidak sepenuhnya mencerminkan kondisi sistem operasi nyata karena        belum mempertimbangkan *context switching* dan waktu tunggu I/O
- Kurang efisien untuk proses dengan burst time pendek karena adanya       *convoy effect*

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
**1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?**

   Simulasi diperlukan untuk menguji algoritma scheduling karena dapat      mengevaluasi kinerjanya secara realistis dengan meniru kondisi kerja     sistem yang sebenarnya, serta memungkinkan perbandingan beberapa         algoritma tanpa harus langsung diterapkan pada sistem operasi nyata.
   
---
**2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?**

   Perhitungan manual pada dataset besar hanya akurat untuk kasus           sederhana dan terbatas, sedangkan simulasi mampu menangani data          yang kompleks dan banyak sehingga hasilnya lebih realistis serta         mendekati kondisi nyata sistem.
   
---
**3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.**

  Algoritma yang paling mudah diimplementasikan adalah First Come First    Served (FCFS). Hal ini karena FCFS menjalankan proses sesuai urutan      kedatangan tanpa perlu perhitungan tambahan seperti prioritas,           prediksi CPU burst, atau preemption. Struktur datanya sederhana, cukup   menggunakan satu antrian (ready queue), sehingga mudah dipahami          dan diterapkan. Namun, meskipun sederhana, FCFS memiliki kelemahan       karena dapat menyebabkan proses pendek menunggu lama jika berada di      belakang proses yang berdurasi panjang.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
