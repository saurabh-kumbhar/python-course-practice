# # convert to list / tuple
# word = "SPK"
# word_list = list(word)
# word_tuple = tuple(word)
#
# print(word)
# print(word_list)
# print(word_tuple)
#
# # range
# for i in range(2, 10, 2):
#     print(i)
#
# # zip. create collection of tuples with itemes in each list
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# chars = ['a', 'b', 'c', 'd', 'e']
#
# for item in zip(nums, chars):  # ignores extra items in nums
#     print(item)
#
# for a,b in zip(nums, chars):  # ignores extra items in nums
#     print(a, ':', b)
#
# print(list(zip(nums,chars)))
# print('---')
# # enumerate. create collection of tuples with index
# for item in enumerate(chars):
#     print(item)
# print('---')
# for item in enumerate(chars, 1):  # start index with 1
#     print(item)

# check values
# print(140 in {'SPK': 140})
# print(140 in {'SPK': 140}.values())

# num_list = [4, 5, 1, 3, 6, 7, 8]
# char_list = ['a', 'c', 'e', 'b', 'd']
# print(min(num_list))
# print(max(num_list))
# print(min(char_list))
# print(max(char_list))

from random import *

print(randint(0, 1000))

num_list = [4, 5, 1, 3, 6, 7, 8]
shuffle(num_list)
print(num_list)

print(random())

print(randrange(0, 1000, 2)) # only even numbers

print(list(range(0, 101, 2)))
