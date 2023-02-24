matrik_A = [
    [2, 2],
    [1, 1]
]

matrik_B = [
    [3, 1],
    [1, 1]
]

matrik_C = []
for x in range(0, len(matrik_A)):
    row = []
    for y in range(0, len(matrik_A[0])):
        total = 0
        for z in range(0, len(matrik_A)):
            total = total + (matrik_A[x][z] * matrik_B[z][y])
        row.append(total)
    matrik_C.append(row)
for x in range(0, len(matrik_C)):
    for y in range(0, len(matrik_C[0])):
        print(matrik_C[x][y], end=" ")
    print()