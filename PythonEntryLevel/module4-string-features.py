laptop = 'MacBook'

print('laptop[3]:', laptop[4])
print('laptop[:3]:', laptop[:3])
print('laptop[3:]:', laptop[3:])

print(laptop.capitalize())
print(laptop.upper())
print(laptop.lower())
print(laptop)

if input('Provide number: ').isnumeric():
    print('It is a number')
else:
    print('It\'s not a number')