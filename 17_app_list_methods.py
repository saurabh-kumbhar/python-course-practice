numbers = [10, 9, 4, 6, 8]

print(numbers)

print("--- append ---")
numbers.append(7)
print(numbers)

print("--- insert ---")
numbers.insert(1,5)
print(numbers)

print("--- remove ---")
numbers.remove(9)
print(numbers)

print("--- pop ---")
numbers.pop()
print(numbers)

print("--- index ---")
print(numbers.index(8))

print("--- in existence---")
print(100 in numbers)

print("--- count ---")
numbers.insert(4,4)
print(numbers.count(4))

print("--- sort ---")
numbers.sort()
print(numbers)

print("--- copy ---")
numbers_copy = numbers.copy()
print(numbers_copy)

print("--- clear ---")
numbers.clear()
print(numbers)


print("--- reverse ---")
numbers_copy.reverse()
print(numbers_copy)


