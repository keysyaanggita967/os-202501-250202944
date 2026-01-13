
# Laporan Praktikum Minggu [12]
Topik: Virtualisasi Menggunakan Virtual Machine

---

## Identitas
- **Nama Anggota Kelompok**  :
1. Faris Azhar(250202978) - Instalasi dan dokumentasi
2. Rafika Rahma (250202917) - Analisis
3. Keysya Ayu Anggita (250202944) - Penyusun laporan dan Quiz

- **Kelas** : 1 IKRA

---

## Tujuan
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).  
2. Membuat dan menjalankan sistem operasi guest di dalam VM.  
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).  
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.  
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.
   
---

## Dasar Teori
**1. Virtualisasi**

Virtualisasi merupakan teknologi yang memungkinkan satu perangkat keras fisik dibagi menjadi beberapa lingkungan komputasi virtual. Setiap lingkungan virtual dapat menjalankan sistem operasi dan aplikasi secara independen, seolah-olah berjalan pada mesin fisik tersendiri, meskipun seluruhnya berbagi sumber daya yang sama.

**2. Virtual Machine (VM)**

Virtual Machine adalah mesin berbasis perangkat lunak yang meniru fungsi perangkat keras komputer. Di dalam virtual machine, sistem operasi tamu dan aplikasinya dapat berjalan tanpa bergantung langsung pada perangkat keras fisik, sehingga memberikan fleksibilitas, isolasi, dan kemudahan dalam pengelolaan sistem.

**3. Oracle VirtualBox**

Oracle VirtualBox adalah hypervisor tipe 2 yang berjalan di atas sistem operasi host dan digunakan untuk membuat serta menjalankan virtual machine, terutama untuk pembelajaran, pengujian, dan pengembangan sistem.

---

## Langkah Praktikum
1. **Instalasi Virtual Machine**
   - Instal VirtualBox atau VMware pada komputer host.  
   - Pastikan fitur virtualisasi (VT-x / AMD-V) aktif di BIOS.

2. **Pembuatan OS Guest**
   - Buat VM baru dan pilih OS guest (misal: Ubuntu Linux).  
   - Atur resource awal:
     - CPU: 1–2 core  
     - RAM: 2–4 GB  
     - Storage: ≥ 20 GB

3. **Instalasi Sistem Operasi**
   - Jalankan proses instalasi OS guest sampai selesai.  
   - Pastikan OS guest dapat login dan berjalan normal.

4. **Konfigurasi Resource**
   - Ubah konfigurasi CPU dan RAM.  
   - Amati perbedaan performa sebelum dan sesudah perubahan resource.

5. **Analisis Proteksi OS**
   - Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.  
   - Kaitkan dengan konsep *sandboxing* dan *hardening* OS.

6. **Dokumentasi**
   - Ambil screenshot setiap tahap penting.  
   - Simpan di folder `screenshots/`.

7. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 12 - Virtual Machine"
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
**1. Apa perbedaan antara host OS dan guest OS?** 
* **Host OS** adalah sistem operasi utama yang berjalan langsung di atas perangkat keras fisik dan mengelola seluruh resource komputer.
* **Guest OS** adalah sistem operasi yang berjalan di dalam mesin virtual dan tidak berinteraksi langsung dengan perangkat keras, karena akses resource komputer    diatur oleh hypervisor.

##
**2. Apa peran hypervisor dalam virtualisasi?**

**Hypervisor** berperan sebagai lapisan perantara antara perangkat keras dan sistem operasi guest. Hypervisor bertugas menciptakan, menjalankan, dan mengelola mesin virtual dengan cara mengalokasikan serta mengendalikan penggunaan sumber daya fisik oleh masing-masing sistem operasi tersebut. Selain itu, hypervisor memastikan bahwa setiap mesin virtual terisolasi sehingga tidak dapat mengganggu mesin virtual lain maupun sistem host.

##
**3. Mengapa virtualisasi meningkatkan keamanan sistem?**

Virtualisasi meningkatkan keamanan karena setiap sistem operasi berjalan dalam lingkungan terisolasi, sehingga gangguan atau serangan pada satu mesin virtual tidak memengaruhi sistem lain maupun sistem utama. 
   

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
