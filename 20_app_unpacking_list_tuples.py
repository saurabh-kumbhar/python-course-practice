# without unpacking
coordinates = (1,2,3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

print(x * y * z)

# with unpacking WORK with LIST and TUPLE
x, y, z = coordinates
print(x * y * z)