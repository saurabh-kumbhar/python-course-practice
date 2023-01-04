# number swapping
# first = input('Enter first number: ')
# second = input('Enter second number: ')
# print('before:', first, second)
# normal way.
# temp = first
# first = second
# second = temp
# print('after: ', first, second)
# Python way!
# first, second = second, first
# print('after:', first, second)

# list swapping
# cities = ['Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Kolhapur']
# print('before:', cities)
# cities[1], cities[0] = cities[0], cities[1]
# print('after:', cities)
#
# sort change list,
# cities.sort()
# print('sorted:', cities)
# cities.sort(reverse=True)
# print('reversed:', cities)

# sorted, return new list
# cities = ['Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Kolhapur']
# print(sorted(cities))
# print(cities)

# Check presence
invited_guests = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'XYZ']
name = input('Enter guest name: ')
# if name in invited_guests:
#     print('Welcome!')
# else:
#     print('Get lost!')

if name not in invited_guests:
    print('Get lost!')
else:
    print('Welcome!')