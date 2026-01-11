
# Laporan Praktikum Minggu [11]
Topik: Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Keysya Ayu Anggita  
- **NIM**   : 250202944
- **Kelas** : 1 IKRA

---

## Tujuan
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.


---

## Dasar Teori
- Deadlock adalah kondisi ketika dua atau lebih proses saling menunggu sumber daya yang sedang digunakan oleh proses lain.
- Deteksi deadlock adalah metode penanganan deadlock dengan cara membiarkan deadlock terjadi lalu mendeteksinya. Sistem operasi melakukan pemeriksaan kondisi       deadlock secara berkala.
- Deteksi deadlock dilakukan dengan menganalisis:
  1) alokasi sumber daya,
  2) permintaan sumber daya,
  3) dan ketersediaan sumber daya.
- Simulasi deadlock adalah pemodelan sistem untuk meniru kondisi pengelolaan proses dan sumber daya. Simulasi dilakukan dengan menjalankan algoritma deteksi terhadap data tersebut. Hasil simulasi menunjukkan proses yang mengalami deadlock dan proses yang dapat diselesaikan.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```

---

## Kode / Perintah

```bash
processes = {
    "P1": {"alloc": "R1", "req": "R2"},
    "P2": {"alloc": "R2", "req": "R3"},
    "P3": {"alloc": "R3", "req": "R1"},
}

resource_owner = {}
for p, data in processes.items():
    resource_owner[data["alloc"]] = p

wait_for = {}
for p, data in processes.items():
    req = data["req"]
    if req in resource_owner:
        wait_for[p] = resource_owner[req]
    else:
        wait_for[p] = None

visited = set()
stack = []
deadlock = set()

def dfs(process):
    if process in stack:
        # Ambil semua proses yang membentuk siklus
        cycle_start = stack.index(process)
        for p in stack[cycle_start:]:
            deadlock.add(p)
        return

    if process in visited or wait_for[process] is None:
        return

    visited.add(process)
    stack.append(process)

    dfs(wait_for[process])

    stack.pop()

# Jalankan DFS untuk setiap proses
for p in wait_for:
    dfs(p)

print("WAIT-FOR GRAPH:")
for p, w in wait_for.items():
    print(f"{p} -> {w}")

print("\nHASIL DETEKSI DEADLOCK:")
if deadlock:
    for p in sorted(deadlock):
        print(f"{p} : DEADLOCK")
else:
    print("Tidak ada deadlock")

```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![alt text](<screenshots/deadlock_week11.png>)

---
## Eksekusi & Validasi
   Dari output program dapat diperoleh relasi sebagai berikut:
   - P1 menunggu P2
   - P2 menunggu P3
   - P3 menunggu P1

Relasi tersebut membentuk siklus tertutup: P1 → P2 → P3 → P1
```bash
    Deadlock terdeteksi pada proses: P1, P2, P3
```

---

## Analisis
**Tabel hasil deteksi deadlock**
| **Proses** | **Allocation** (resource yang dipegang)| **Request** (resource yang dibutuhkan) |  **Status** |
| --- | --- | --- | --- |
| P1 | R1 | R2 | Deadlock |
| P2 | R2 | R3 | Deadlock |
| P3 | R3 | R1 | Deadlock |

##
Seluruh proses berada dalam kondisi deadlock karena masing-masing proses saling menunggu resource yang sedang digunakan oleh proses lain, sehingga tidak ada satu pun proses yang dapat melanjutkan eksekusinya. Proses P1 menggunakan resource R1 dan menunggu resource R2 yang dikuasai oleh P2, sementara P2 menggunakan resource R2 dan menunggu resource R3 yang dikuasai oleh P3. Pada saat yang sama, P3 menggunakan resource R3 dan menunggu resource R1 yang dikuasai oleh P1. Pola saling menunggu ini membentuk circular wait yang menyebabkan sistem mengalami kebuntuan permanen atau deadlock.

##
**Kaitkan hasil dengan teori deadlock (empat kondisi).**

Deadlock terjadi karena keempat kondisi deadlock terpenuhi secara persamaan, yaitu:
- **Mutual Exclusion** : Proses tidak dapat menggunakan resource secara bersamaan, sehingga harus menunggu giliran.
- **Hold and Wait** : Setiap proses menahan apa yang dimilikinya sambil menunggu proses lain.
- **No Preemption** : Sistem tidak dapat mengambil paksa apa yang sedang dipegang proses.
- **Circular Wait** : Terjadi rantai menunggu melingkar antara P1, P2, dan P3.
 
---

## Kesimpulan
- Hasil praktikum membuktikan bahwa adanya circular wait antar proses menyebabkan sistem tidak dapat melanjutkan eksekusi dan seluruh proses teridentifikasi        dalam kondisi deadlock.
- Simulasi dan deteksi deadlock memberikan pemahaman yang jelas mengenai bagaimana interaksi alokasi dan permintaan resource dapat menimbulkan kebuntuan pada       sistem.
- Algoritma deteksi deadlock efektif untuk mengidentifikasi proses-proses yang terlibat dalam deadlock, sehingga dapat digunakan sebagai dasar pengambilan          tindakan pemulihan pada sistem operasi.

---

## Quiz
**1. Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*?**
   | **Pendekatan Deadlock** | **Tujuan** | **Cara Kerja** | **Dampak pada sistem** |
   | --- | --- | --- | --- |
   | *Deadlock Prevention* | Mencegah deadlock sejak awal | Menghilangkan salah satu dari empat kondisi deadlock | Utilisasi resource cenderung rendah |
   | *Avoidance* | Menghindari deadlock dengan menjaga sistem tetap pada safe state | Mengevaluasi setiap permintaan resource sebelum diberikan | Utilisasi lebih       baik dibanding prevention |
   | *Detection* | Mendeteksi deadlock setelah terjadi | Membiarkan deadlock terjadi lalu menjalankan algoritma deteksi | Utilisasi resource tinggi |

##

**2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?**
   
   Deteksi deadlock diperlukan karena banyak sistem operasi tidak mencegah atau menghindari deadlock, melainkan membiarkannya terjadi lalu mendeteksi dan            memulihkannya, agar penggunaan resource tetap efisien pada sistem yang dinamis.
   
##

**3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?**
   
   - **Kelebihan:** deteksi deadlock tidak membatasi penggunaan resource sehingga pemanfaatan resource sistem lebih optimal.
   - **Kekurangan:** deadlock tetap terjadi dan proses deteksi serta pemulihannya menimbulkan overhead serta dapat mengganggu eksekusi proses.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
