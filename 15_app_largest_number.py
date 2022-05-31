numbers = [1, 5, 7, 2, 4, 9, 3, 8]

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number

print(f"Largest number: {largest_number}")
