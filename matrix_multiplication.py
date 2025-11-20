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

# Multiplying using for loop
for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):
            C[i][j] += A[i][k] * B[k][j]

print("Resultant Matrix (A × B):")
for row in C:
    print(row)
