matrik_A = [
    [1, 2],
    [3, 4]
]

matrik_B = [
    [2, 2],
    [2, 2]
]

for x in range(0, len(matrik_A)):
    for y in range(0, len(matrik_A[0])):
        print(matrik_A[x][y] + matrik_B[x][y], end=" "),
    print