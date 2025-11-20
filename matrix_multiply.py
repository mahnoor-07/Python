A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

rows1 = len(A)
cols1 = len(A[0])
rows2 = len(B)
cols2 = len(B[0])

if cols1 != rows2:
    print("Matrix multiplication NOT possible")
    exit()

# Result matrix
C = [
    [0, 0],
    [0, 0]
]

# Multiplying using WHILE loops
i = 0
while i < rows1:
    j = 0
    while j < cols2:
        k = 0
        while k < cols1:
            C[i][j] += A[i][k] * B[k][j]
            k += 1
        j += 1
    i += 1

print("Resultant Matrix (A × B):")
for row in C:
    print(row)
