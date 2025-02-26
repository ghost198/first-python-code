# program perulangan while sampai paham

jumlah_buku = 10
print('perintah ibu, "baca semua bukumu"')

total_jumlah_baca = 0

jumlah_buku_yang_dibaca_dan_dipahami = 0
print(f'baik bu, "saat in'
      f'i jumlah buku yang belum saya baca dan pahami" {jumlah_buku_yang_dibaca_dan_dipahami}')
print("saya akan mulai membaca")

while total_jumlah_baca < jumlah_buku + 2 :
    total_jumlah_baca = total_jumlah_baca +1
    if jumlah_buku_yang_dibaca_dan_dipahami == 9:
        print(f"buku ke {jumlah_buku_yang_dibaca_dan_dipahami + 1} belum paham")
    else:
        jumlah_buku_yang_dibaca_dan_dipahami = jumlah_buku_yang_dibaca_dan_dipahami + 1
        print(f"buku ke {jumlah_buku_yang_dibaca_dan_dipahami} sudah saya baca dan pahami")
if jumlah_buku_yang_dibaca_dan_dipahami == jumlah_buku:
    print("semua buku sudah saya baca dan pahami")
else:
    print(f"maaf bu, tidak semua buku bisa saya baca dan pahami")

print(f'jumlah buku yang sudah dibaca dan pahami hanya {jumlah_buku_yang_dibaca_dan_dipahami} buku')
