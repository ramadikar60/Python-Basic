nim = int(input("Nomor Induk Mahasiswa = "))
namamhs = str(input("Nama Mahasiswa = "))
nilaipy = int(input("Nilai Python = "))

if nilaipy >= 80:
    index = "A"
elif nilaipy < 80 and nilaipy >= 70:
    index = "B"
elif nilaipy < 70 and nilaipy >= 55:
    index = "C"
elif nilaipy < 55 and nilaipy >= 40:
    index = "D"
else:
    index = "E"

if index == "A":
    keterangan = "Lulus"
elif index == "B":
    keterangan = "Lulus"
elif index == "C":
    keterangan = "Lulus"
elif index == "D":
    keterangan = "Lulus"
else:
    keterangan = "Gagal"

print("==================================")
print("Nomor Induk Mahasiswa =", nim)
print("Nama Mahasiswa =", namamhs)
print("Nilai Python =", nilaipy)
print("Mutu Huruf =", index)
print("Keterangan =", keterangan)