orang = {"nama": "rama dika", "kota": "jakarta", "umur": "19"}
try:
    contact = open("contact.txt", "r")
    print(orang["pekerjaan"])
except KeyError as err:
    print("Terjadi kesalahan pada list/dict/tuples: ", err)
finally:
    print("baris ini akan selalu di eksekusi")
print(orang)