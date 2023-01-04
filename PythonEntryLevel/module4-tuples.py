# e_tuple = ()
# a_tuple = 1,
# b_tuple = (1,)
# c_tuple = 1, 2
# print(e_tuple)
# print(a_tuple)
# print(b_tuple)
# print(c_tuple)
#
# # tuples are mutable like strings unlike lists
# user = ('SPK', 1991, 'Pune')
# print(user)
# # del user[0] # not allowed
# # user[0] = 'SPK' # not allowed
#
# user = ('SPK', 1991, 'Pune') + ('IT Wala', 'Male')
#
# print(len(user))
# if 'Pune' in user:
#     print('Punekar!')
#
# for item in user:
#     print(item)
#
# num = (0, 1) * 2
# print(num)

# # list of tuples
# cities = [('Pune', 1), ('Mumbai', 2), ('Nagpur', 3)]
# print(cities)

# list in tuple is mutable
user = ('SPK', 1991, 'Pune', [6.2, 6.8, 12.5, 19.5])
print(user)
user[3].append(35)
print(user)
