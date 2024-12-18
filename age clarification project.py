umur = int(input("Masukkan Umur Anda :"))

if umur >= 0 and umur <= 2:
    kategori = "Bayi"
elif umur >= 3 and umur <= 12:
    kategori = "Anak-anak"
elif umur >= 13 and umur <= 19:
    kategori = "Remaja"
elif umur >= 20 and umur <= 35:
    kategori = "Dewasa"
elif umur >= 36 and umur <= 50:
    kategori = "Paruh Baya"
else:
    kategori = "Lansia"

print("Anda sekarang berada dalam kategori usia :", kategori)

