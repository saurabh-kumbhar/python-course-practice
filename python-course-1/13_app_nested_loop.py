for x in range(1,3):
    for y in range(1,3):
        print(f"({x}, {y})")

print("-" * 20)

print("Print E")
numbers = [6, 2, 6, 2, 6]
print("Single for loop")
for number in numbers:
    print("X" * number)
print("Nested for loop")
for x_counts in numbers:
    line = ""
    for count in range(x_counts):
        line += "X"
    print(line)
print("While inside for loop")
for number in numbers:
    count = 0
    line = ""
    while count < number:
        count += 1
        line += "X"
    print(line)
