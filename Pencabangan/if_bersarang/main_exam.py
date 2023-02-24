qty = int(input("Banyak Barang = "))
hrgbrg = int(input("Harga Satuan = "))
jmlbyr = qty * hrgbrg
if jmlbyr > 300000:
    if hrgbrg > 50000:
        keterangan = "Tidak dapat kartu diskon"
    else:
        keterangan = "Dapat kartu diskon"
else:
    keterangan = "Dapat kartu diskon"

if qty > 100:
    diskon = jmlbyr * 0.3
else:
    diskon = 0

byrakh = jmlbyr - diskon

print("Banyak Barang =", qty)
print("Harga Satuan =", hrgbrg)
print("Keterangan =", keterangan)
print("Total Bayar Akhir =", byrakh)