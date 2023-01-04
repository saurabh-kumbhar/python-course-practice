# Copy string (same applicable to all, int, float, bool etc but not list
# name = 'SPK'
# new_name = name
#
# print('before...')
# print('name', name)
# print('new_name', new_name)
#
# name = 'PSK'
# print('after...')
# print('name', name)
# print('new_name', new_name)

# Copy list
# cities = ['Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Kolhapur']
# same_cities = cities
# new_cities = cities[:]
# OR
# new_cities = cities.copy()
# OR part of list
# new_cities = [:4]

# print('before...')
# print('cities', cities)
# print('same_cities', same_cities)
# print('new_cities', new_cities)
#
# cities.append('Sangli')
# new_cities.insert(3, 'Sangli')
#
# print('after...')
# print('cities', cities)
# print('same_cities', same_cities)
# print('new_cities', new_cities)

# Comprehension

# normal way
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# for i in range(6, 101):
#     numbers.append(i)
# print(numbers)

# python way
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# numbers = [i for i in range(6, 101)]
# print(numbers)

# Even numbers from 1 to 100
even_num = [i for i in range(1,101) if i % 2 == 0]
print('even_num', even_num)
odd_num = [i for i in range(1,101) if i % 2 != 0]
print('odd_num', odd_num)
