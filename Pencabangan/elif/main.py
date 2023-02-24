lama = int(input("Lama menginap = "))
harga = int(input("Harga kamar = "))
jumlah = lama * harga
if jumlah > 300000:
    diskon = jumlah * 0.3
elif jumlah > 200000 and jumlah <= 300000:
    diskon = jumlah * 0.2
elif jumlah > 100000 and jumlah <= 200000:
    diskon = jumlah * 0.1
else:
    diskon = 0

if diskon > 0:
    keterangan = "Dapat diskon"
else:
    keterangan = "Tidak diskon"

bayar = jumlah - diskon
print("Bayar = ", bayar)
print("Keterangan =", keterangan)