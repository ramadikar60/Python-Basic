while True:
    nama = input("Masukkan Nama: ")
    npm = input("Masukkan NPM: ")
    if len(npm) != 8:
        print("NPM tidak sesuai")
        continue
    ang = npm[3:5]
    jur = npm[0]
    if npm[3] == '9':
        ang = '19' +ang
    elif npm[3] == '0':
        ang = '20' +ang
    elif npm[3] == "1":
        ang = "20" +ang
    else:
        print("NPM Salah\n")
        continue
    print(ang)
    if jur == '1':
        jur = 'D3-TI'
    elif jur == '2':
        jur = 'S1-ST'
    elif jur == '3':
        jur = 'S1-SK'
    elif jur == '4':
        jur = 'S1-TI'
    elif jur == '5':
        jur = 'S1-SI'
    elif jur == '6':
        jur = 'D3-SK'
    elif jur == '7':
        jur = 'S1-TK'
    elif jur == '8':
        jur = 'S1-TM'
    elif jur == '9':
        jur = 'S1-IK'
    else:
        print('NPM Salah\n')
        continue
    print('=========================================================')
    print(nama)
    print('Mahasiswa jurusan %s dan angkatan tahun %s'%(jur, ang))
    lagi = ''
    while lagi != 'y' and lagi != 't':
        lagi = input('Coba lagi [y/t]')
    if lagi == 't':
        break
