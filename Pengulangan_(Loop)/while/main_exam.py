A = int(input("Angka Bilangan A = "))
B = int(input("Angka Bilangan B = "))

F = 1
i = 1

while i <= B:
    F = F * A
    i = i + 1

print("F =", F)