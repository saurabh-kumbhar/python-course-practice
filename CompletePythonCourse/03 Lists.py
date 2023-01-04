# LIST
# my_list = [1, 2, 3, 4, 5]
# print(type(my_list))
# print('my_list:', my_list)
#
#
# print('my_list.pop(): popped', my_list.pop(), '| Result: ', my_list)
#
# my_list.pop(0)
# print('my_list.pop(0):', my_list)
#
# my_list[0] = ['str', 'array']
# print("my_list[0] = ['str', 'array']:", my_list)
#
# my_list.append('last item in array')
# print("my_list.append('last item in array')", my_list)

# my_list = [3, 2, 4, 1, 5]
# print('my_list:', my_list)
#
# my_list.sort()
# print('my_list.sort():', my_list)
#
# my_list.reverse()
# print('my_list.reverse():', my_list)


# my_list = ['3', 'b', '2', '4', '#', '1', '5', 'a']
# print('my_list:', my_list)
#
# my_list.sort()
# print('my_list.sort():', my_list)
#
# my_list.reverse()
# print('my_list.reverse():', my_list)

# list_al = ['a', 'b', 'c']
# list_num = [1, 2, 3]
# print('list_al + list_num', list_al + list_num)
# my_list = list_al + list_num
# print('my_list', my_list)
# list_al.append(list_num)
# print('list_al.append(list_num) ', list_al)

# None
# print(type(None))

# assignment 1  reverse sort and extract last 3 elemenets from 2 list into 1
# my_list = ['b', 'd', 'a', 'z', 'x']
# another_list = [1, 2, 3, 4, 5]
#
# my_list.sort()
# my_list.reverse()
# another_list.reverse()
# print(my_list[-3:] + another_list[-3:])

# assignment 2 extract robert
my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', ['john', 'robert'], 'banana'], 'd', 1, 2, 1, 1]
print(my_list[6][2][1])
my_list[6][2][1] = 'joe'
print(my_list)

print(my_list.index('d'))
print(my_list[6].index('banana'))
print(my_list[6][2].index('john'))
print(my_list.count(1))