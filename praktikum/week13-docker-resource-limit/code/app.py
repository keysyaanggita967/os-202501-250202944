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
