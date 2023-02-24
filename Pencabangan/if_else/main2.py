lama = int(input("Lama Menginap = "))
harga = int(input("Harga Kamar = "))
jumlah = lama * harga
if jumlah > 1000000:
    diskon = jumlah * 0.1
    keterangan = "Anda dapat diskon"
else:
    diskon = 0
    keterangan = "Anda tidak dapat diskon"
bayar = jumlah - diskon
print("Bayar =", bayar)
print("Keterangan =", keterangan)