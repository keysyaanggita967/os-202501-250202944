
# Laporan Praktikum Minggu [14]
**Penyusunan Laporan IMRAD**

---

## Identitas
- **Nama**  : Keysya Ayu Anggita 
- **NIM**   : 250202944 
- **Kelas** : 1 IKRA

---
# Analisis Deadlock Detection 
## 1. Pendahuluan (Introduction)

**1.1 Latar Belakang**

Deadlock adalah kondisi pada sistem operasi ketika beberapa proses saling menunggu sumber daya yang sedang digunakan oleh proses lain, sehingga tidak ada       proses yang dapat melanjutkan eksekusinya. Keadaan ini dapat menyebabkan sistem menjadi tidak responsif dan menurunkan kinerja secara keseluruhan. Oleh sebab      itu, diperlukan mekanisme deadlock detection untuk mengenali terjadinya deadlock setelah sistem berjalan, agar dapat dilakukan tindakan pemulihan seperti          penghentian   atau penjadwalan ulang proses tertentu (*Silberschatz et al., 2018*).

Tanenbaum dan Bos (2015) menjelaskan bahwa deadlock detection umumnya diterapkan pada sistem yang tidak menerapkan pencegahan deadlock sejak awal. Mekanisme       ini   memberikan keleluasaan dalam penggunaan sumber daya, namun tetap membutuhkan algoritma yang efektif agar deadlock dapat teridentifikasi dan tidak            mengganggu stabilitas sistem.

Untuk memperjelas pemahaman mengenai konsep deadlock, diperlukan suatu simulasi yang menunjukkan proses terjadinya deadlock secara nyata. Oleh karena itu, pada praktikum ini digunakan program sederhana berbasis Python sebagai media simulasi, sehingga mahasiswa dapat mengamati secara langsung terjadinya deadlock serta mengetahui faktor-faktor yang menyebabkannya.


**1.2 Rumusan Masalah**
1. Apa yang dimaksud dengan deadlock dalam sistem operasi?
2. Bagaimana deadlock dapat terjadi antar proses yang berjalan dalam sistem?
3. Bagaimana mekanisme deadlock detection bekerja dalam mendeteksi kondisi deadlock?
4. Bagaimana simulasi deadlock menggunakan program Python dapat menggambarkan terjadinya deadlock?

**1.3 Tujuan**
1. Menjelaskan pengertian deadlock dalam sistem operasi.
2. Menjelaskan penyebab terjadinya deadlock antar proses.
3. Memahami cara kerja deadlock detection dalam mendeteksi deadlock.
4. Mensimulasikan kondisi deadlock menggunakan program berbasis Python untuk mengamati proses terjadinya deadlock secara langsung.

## 2. Metode (Methods)

**2.1 Lingkungan Uji**
- Sistem Operasi : mas OS
- Bahasa Pemograman dan versi : Python 3.9.0 (64-bit)
- Alat bantu : Visual Studio Code atau terminal
- Library :  `threading`, `time`
  
**2.2 Langkah eksperimen**
1. Menyiapkan lingkungan dan membuat file program Python.
2. Mendefinisikan dua resource berupa `Lock A` dan `Lock B`.
3. Membuat dua thread dengan urutan penguncian resource yang berbeda.
4. Menambahkan jeda waktu (`sleep`) untuk memicu deadlock.
5. Menjalankan kedua thread secara bersamaan.
6. Mengamati program berhenti dan tidak selesai akibat deadlock.

**2.3 Implementasi Program (Python)**
``` bash
import threading
import time

lock_A = threading.Lock() # Dua resource (lock)
lock_B = threading.Lock()

def proses_1():
    print("Proses 1: mencoba mengunci Lock A")
    lock_A.acquire()
    print("Proses 1: Lock A berhasil dikunci")

    time.sleep(1)  # simulasi proses

    print("Proses 1: mencoba mengunci Lock B")
    lock_B.acquire()
    print("Proses 1: Lock B berhasil dikunci")

    lock_B.release()
    lock_A.release()

def proses_2():
    print("Proses 2: mencoba mengunci Lock B")
    lock_B.acquire()
    print("Proses 2: Lock B berhasil dikunci")

    time.sleep(1)  # simulasi proses

    print("Proses 2: mencoba mengunci Lock A")
    lock_A.acquire()
    print("Proses 2: Lock A berhasil dikunci")

    lock_A.release()
    lock_B.release()

t1 = threading.Thread(target=proses_1) # Membuat thread
t2 = threading.Thread(target=proses_2)

t1.start() #Menjalankan thread
t2.start()

t1.join() #Menunggu thread selesai
t2.join()

print("Program selesai")

```

## 3. Hasil (Results)
![alt text](<screenshots/deadlock_week14.png>)
Berdasarkan hasil eksekusi program, terjadi kondisi deadlock ketika dua proses saling mengunci resource yang berbeda dan kemudian saling menunggu resource milik proses lain. Akibatnya, kedua proses terhenti dan program tidak dapat selesai secara normal.

## 4. Pembahasan (Discussion)
**4.1 Interpretasi Hasil**

Dari hasil eksekusi terlihat bahwa program mengalami deadlock.
- Proses 1 berhasil mengunci Lock A, lalu mencoba mengunci Lock B.
- Proses 2 berhasil mengunci Lock B, lalu mencoba mengunci Lock A.
- Kedua proses saling menunggu resource yang sedang dipegang proses lain. Akibatnya, tidak ada proses yang bisa lanjut dan program berhenti tanpa selesai.
Artinya, sistem berhenti pada kondisi kebuntuan(deadlock).

**4.2 Keterbatasan**

Beberapa keterbatasan dari percobaan ini:
1. Tidak ada timeout atau rollback, jadi proses akan menunggu selamanya.
2. Contoh ini hanya menggunakan dua proses dan dua lock, sedangkan di sistem nyata deadlock bisa melibatkan lebih banyak resource.
3. Program tidak memiliki mekanisme deteksi deadlock, sehingga deadlock hanya bisa diketahui dari output yang berhenti.

**4.3 Perbandingan Teori dengan Hasil Eksekusi**

Menurut teori deadlock:
* *Mutual Exclusion*: Lock hanya bisa dipakai satu proses
* *Hold and Wait*: Proses memegang lock sambil menunggu lock lain
* *No Preemption*: Lock tidak bisa direbut paksa
* *Circular Wait*: Proses 1 menunggu Proses 2, dan sebaliknya

Menurut eksekusi program:
* Keempat kondisi tersebut terjadi secara nyata
* Urutan penguncian yang berbeda menyebabkan circular wait
* Hasil eksekusi sesuai dengan teori deadlock dalam sistem operasi

## 5. Kesimpulan
- Deadlock terjadi karena dua proses mengunci resource yang berbeda lalu saling menunggu resource milik proses lain.
- Urutan penguncian resource yang tidak konsisten menyebabkan circular wait.
- Seluruh kondisi deadlock (Coffman) terpenuhi pada eksekusi program.
- Akibat deadlock, proses tidak dapat dilanjutkan dan program tidak selesai secara normal.
- Hasil eksekusi program sesuai dengan teori deadlock dalam sistem operasi.

---
---

## Quiz
**1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?**
   
   Format IMRAD membuat laporan lebih ilmiah dan mudah dievaluasi karena menyajikan informasi secara terstruktur: pendahuluan menjelaskan tujuan dan latar           belakang, metode memaparkan prosedur yang dapat diikuti ulang, hasil menyajikan data secara objektif, dan diskusi menjelaskan arti dan implikasi dari hasil       percobaan.
   
**2. Apa perbedaan antara bagian **Hasil** dan **Pembahasan**?**
- Hasil (Results): Menyajikan data atau temuan percobaan secara objektif tanpa interpretasi. Contohnya, output program.
- Pembahasan (Discussion): Menafsirkan hasil, menjelaskan alasan terjadinya hasil tersebut, membandingkan dengan teori atau sumber referensi, serta mengevaluasi keterbatasan percobaan.
  
**3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?**

  Untuk menghindari plagiarisme dan memperkuat laporan, sitasi dan daftar pustaka digunakan untuk memberikan pengakuan terhadap sumber teori atau informasi yang    digunakan, memudahkan pembaca menelusuri sumber referensi, serta membuat laporan lebih ilmiah dan terpercaya.

---
## Daftar Pustaka
1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
2. Tanenbaum, A. S., & Bos, H. (2015). *Modern Operating Systems* (4th ed.). Pearson Education
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
