deret = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 10, 20, 20, 20]
print("\n=========================")
print("Akses list per indeks: ")
print(deret[1])
print(deret[3])
print(deret[6])
print(deret[9])
print("\n=========================")
print("Mencacah isi list: ")
for x in deret:
    print(x)
print("\n=========================")
print("Panjang list: ", str(len(deret)))
print("\n=========================")
print("Banyaknya angka 20: ", str(deret.count(20)))
print("\n=========================")
print("Menambah element list dengan append: ")
deret.append(15)
deret.append(17)
deret.append(24)
deret.append(67)
print(deret)
print("Panjang listnya jadi: ", str(len(deret)))
print("\n=========================")
print("Mencari indeks suatu nilai dengan index: ")
print("Nilai 100 ada di index:", deret.index(100))
print("Nilai 15 ada di index:", deret.index(15))
print("Nilai 10 ada di index:", deret.index(10))
print("Nilai 17 ada di index:", deret.index(17))
print("Nilai 67 ada di index:", deret.index(67))
print("\n=========================")
print("Menambah element list dengan insert: ")
deret.insert(2, 43)
deret.insert(2, 75)
deret.insert(2, 84)
deret.insert(10, 85)
print(deret)
print("\n=========================")
print("Membuang element list dengan pop: ")
deret.pop()
deret.pop()
deret.pop()
print(deret)
print("\n=========================")
print("Membuang element list dengan remove: ")
deret.remove(43)
deret.remove(75)
deret.remove(84)
deret.remove(85)
print(deret)
print("\n=========================")
print("Menambah element list dengan extend: ")
deret2 = [1, 2, 3, 4, 5]
deret.extend(deret2)
print(deret)
print("\n=========================")
print("Membalik list dengan reverse: ")
deret.reverse()
print(deret)
print("\n=========================")
print("Mengurutkan list dengan sort: ")
deret.sort()
print(deret)
print("\n=========================")
print("Mencari nilai max dari list: ")
print(max(deret))
print("\n=========================")
print("Mencari nilai min dari list: ")
print(min(deret))
print("\n=========================")
print("Mencari nilai sum dari list: ")
print(sum(deret))