namapgw = str(input("Nama Pegawai = "))
gapok = int(input("Gaji Pokok = "))
jmljamkj = int(input("Jumlah Jam Kerja = "))

gator = gapok * jmljamkj
if gator >= 500000:
    tax = gator * 0.05
    keterangan = "Pajak"
else:
    tax = 0
    keterangan = "Tidak Pajak"

gaber = gator - tax

print("Gaji Kotor = ", gator)
print("Pajak = ", tax)
print("Gaji Bersih = ", gaber)
print("Keterangan = ", keterangan)