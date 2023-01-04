my_tuple = (1, 2, 3, 'a', 'b', 'c', 'def', ['list', 'in', 'tuple'], (6, 7, 8, 9, 'tuple', 'in', 'tuple'))
print(my_tuple)

print('type(my_tuple):', type(my_tuple))
print('type(my_tuple[7]):', type(my_tuple[7]))
print('type(my_tuple[7][1]):', type(my_tuple[7][1]))


# my_tuple[1] = 1 # not allowed

my_tuple[7][1] = 'inside'
print(my_tuple)

# tuple immutable but supports indexing and slicing
