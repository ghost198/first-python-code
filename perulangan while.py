# program perulangan while

jumlah_buku = 10
print('perintah ibu, "baca semua bukumu"')

jumlah_buku_yang_dibaca = 0
print(f'baik bu, "saat ini jumlah buku yang belum saya baca" {jumlah_buku_yang_dibaca}')
print("saya akan mulai membaca")

while jumlah_buku_yang_dibaca < jumlah_buku:
    jumlah_buku_yang_dibaca = jumlah_buku_yang_dibaca +1
    print(f"buku ke {jumlah_buku_yang_dibaca} sudah saya baca")

print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_dibaca}')
