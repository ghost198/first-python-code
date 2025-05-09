# program perulangan membaca buku for
jumlah_buku = 10
print('perintah ibu, "Baca semua bukumu"')

jumlah_buku_yang_dibaca = 0
print(f'baik bu, "saat ini buku yang belum saya baca" {jumlah_buku_yang_dibaca}')
print("saya akan mulai membaca")
print("test, halo")

for jumlah_buku_yang_dibaca in range(1, jumlah_buku+1):
    print(f"buku ke {jumlah_buku_yang_dibaca} sudah dibaca ")

print(f"jumlah buku yang sudah dibaca {jumlah_buku_yang_dibaca}")