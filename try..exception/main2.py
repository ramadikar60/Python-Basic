orang = {"nama": "rama dika", "kota": "jakarta", "umur": "19"}
try:
    contact = open("contact.txt", 'r')
    print(orang["pekerjaan"])
except IOError as err:
    print("Terjadi error IO: ", err)
except KeyError as err:
    print("Terjadi kesalahan pada akses list/dict/tuples: ", err)
print(orang)