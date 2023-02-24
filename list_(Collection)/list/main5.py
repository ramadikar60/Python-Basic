npm = []
nama = []
uts = []
uas = []
total = []
data = int(input('Masukkan Banyak Data : '))
print('=========================')
for i in range(data):
    a = input('Masukkan NPM Anda : ')
    npm.append(a)
    b = input('Masukkan Nama Anda : ')
    nama.append(b)
    c = float(input('Masukkan nilai UTS : '))
    uts.append(c)
    d = float(input('Masukkan nilai UAS : '))
    uas.append(d)
    print('================================')

for i in range(data):
    e = (0.7 * uts[i]) + (0.3 * uas[i])
    total.append(round(e, 4))
    # total.append(e)

for i in range(data):
    print('')
    print('           Data Mahasiswa         ')
    print('==================================')
    print('Nama                :', nama[i])
    print('NPM                 :', npm[i])
    print('Nilai UTS           :', uts[i])
    print('Nilai UAS           :', uas[i])
    print('Total Nilai         :', total[i])
    print('')