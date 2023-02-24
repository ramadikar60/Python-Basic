def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

a = int(input("A = "))
fak = faktorial(a)
print("Faktorial =", fak)