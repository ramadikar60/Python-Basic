nm = input('Nama : ')
pwd = input('Password : ')
hobby = []
other = {}
i = 0
while True:
    hobby.append(input('Hobby Anda : '))
    lagi = ''
    while lagi != 'y' and lagi != 't':
        lagi = input('Masih ada lagi [Y/T] : ')
    if lagi == 't':
        break
    i+=1
other['Sex'] = input('Jenis Kelamin : ')
other['TTL'] = input('Tempat/Tanggal Lahir : ')
other['Umur'] = input('Umur : ')
def guest(name, password, *hobby, **other):
    print("Your name : ", name)
    print("Your Password : ", password)
    print("Hobby Anda : ")
    for n in range(i + 1):
        print(hobby[n])
    print("Lain-lain : ")
    print(other['Sex'])
    print(other['TTL'])
    print(other['Umur'])
guest(nm, pwd, *hobby, **other)