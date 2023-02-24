print("=======================")
print("PROGRAM KALKULASI GAJI")
print("=======================")
print("=======================")
print("| Pilih Jabatan       |")
print("=======================")
print("| 1. System Analyst   |")
print("| 2. Programmer       |")
print("| 3. Operator         |")
print("| 4. Other            |")
print("| 5. Exit             |")
print("=======================")
pilih = int(input("Masukkan Pilihan Anda : "))
print("==========================")
if pilih == 1:
    print("")
    print("Kalkulasi Gaji System Analyst")
    gaji = 8000000
    tunjangan = 0.25 * gaji
    ppn = 0.1 * gaji
    total = (gaji + tunjangan) - ppn
    print("================================")
    print("| Gaji Pokok :", gaji, "        |")
    print("| Tunjangan :", tunjangan, "       |")
    print("| Pajak Penghasilan :", ppn, "|")
    print("================================")
    print("Total Gaji Sytem Analyst : ", "Rp.", total)
elif pilih == 2:
    print("")
    print("Kalkulasi Gaji Programmer")
    gaji = 7000000
    tunjangan = 0.125 * gaji
    ppn = 0.1 * gaji
    total = (gaji + tunjangan) - ppn
    print("================================")
    print("| Gaji Pokok :", gaji, "        |")
    print("| Tunjangan :", tunjangan, "        |")
    print("| Pajak Penghasilan :", ppn, "|")
    print("================================")
    print("Total Gaji Programmer : ", "Rp.", total)
elif pilih == 3:
    print("")
    print("Kalkulasi Gaji Operator")
    gaji = 5200000
    tunjangan = 0.16 * gaji
    ppn = 0.1 * gaji
    total = (gaji + tunjangan) - ppn
    print("================================")
    print("| Gaji Pokok :", gaji, "        |")
    print("| Tunjangan :", tunjangan, "        |")
    print("| Pajak Penghasilan :", ppn, "|")
    print("================================")
    print("Total Gaji Operator : ", "Rp.", total)
elif pilih == 4:
    print("")
    print("Kalkulasi Gaji Other")
    gaji = 5000000
    tunjangan = 0.16 * gaji
    ppn = 0.1 * gaji
    total = (gaji + tunjangan) - ppn
    print("================================")
    print("| Gaji Pokok :", gaji, "        |")
    print("| Tunjangan :", tunjangan, "        |")
    print("| Pajak Penghasilan :", ppn, "|")
    print("================================")
    print("Total Gaji Other : ", "Rp.", total)
elif pilih == 5:
    print("Terima kasih telah menggunakan program kalkulasi gaji sederhana ini.")
else:
    print("Nomor yang anda input SALAH!")