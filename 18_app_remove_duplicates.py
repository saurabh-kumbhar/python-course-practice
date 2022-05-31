numbers = [10, 5, 9, 4, 6, 8, 7, 4, 5, 10]
unique_list = []

for number in numbers:
    if number not in unique_list:
        unique_list.append(number)

print(unique_list)
