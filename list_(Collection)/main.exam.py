n = int(input("Jumlah pembeli? "))

nm = []
qty = []
hrgbr = []
jmlbyr = []
disc = []
byrakh = []

for i in range(n):
    print("Pembeli ke-", i+1)
    nm.append(input("Nama pembeli? "))
    qty.append(int(input("Banyak barang? ")))
    hrgbr.append(int(input("Harga satuan? ")))
    jmlbyr.append(qty[i] * hrgbr[i])
    if jmlbyr[i] > 600000:
        disc.append(0.2)
    elif jmlbyr[i] > 400000:
        disc.append(0.15)
    elif jmlbyr[i] > 200000:
        disc.append(0.1)
    else:
        disc.append(0)
    byrakh.append(jmlbyr[i] * (1 - disc[i]))

total = 0
for i in range(n):
    total += byrakh[i]

print("Total bayar akhir:")
for i in range(n):
    print(nm[i], ": Rp", byrakh[i])
print("Jumlah seluruh total bayar akhir:", total)