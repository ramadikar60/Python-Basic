qty = int(input("Banyak Barang = "))
harga = int(input("Harga Barang = "))
jumlah = qty * harga
if jumlah > 1000000:
    diskon = jumlah * 0.1
else:
    diskon = 0

bayar = jumlah - diskon
print("Bayar = ", bayar)