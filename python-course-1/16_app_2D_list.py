matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("-" * 10)

print(matrix)
print(matrix[0])
print(matrix[0][1])

print("-" * 10)

matrix [0][0] = 0
print(matrix)
matrix [0][0] = 1
print(matrix)

print("-" * 10)

for row in matrix:
    print(row)

print("-" * 10)

for row in matrix:
    for item in row:
        print(item)

print("-" * 10)