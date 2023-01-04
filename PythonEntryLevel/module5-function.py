# def greet(name):
#     print('Hello, ', name, '!', sep='')
#
#
# def find_average(input_num):
#     sum = 0.0
#     for number in input_num:
#         sum += number
#     average = sum / len(input_num)
#     print(average)
#
#
# def print_letter_count(text, letter='A'):
#     count = 0
#     for c in text:
#         if c == letter:
#             count += 1
#     return count
#
#
# greet('SPK')
# find_average([5.0, 7.4, 5.3, 9.5, 8.6, 1.6])
# # default param
# print(print_letter_count('A for Apple, A for Access', letter='e'))
# print(print_letter_count('A for Apple, A for Access'))

# name scopes
# def show_text():
#     pass_var = 'dest value' # shadowed local variable, changes locally
#     print(pass_var)
#
#
# pass_var = 'source value' # defined before function, so in a scope
# print(pass_var)
# show_text()
# print(pass_var) # doesn't affect due to show_text() assignment

# try to avoid this
# def show_text():
#     global pass_var
#     pass_var = 'dest value' # shadowed defined as global variable, changes globally
#     print(pass_var)
#
#
# pass_var = 'source value' # defined before function, so in a scope
# print(pass_var)
# show_text()
# print(pass_var) # does affect due to show_text() 'global' assignment

# list with shadowing, name scope
# def show_text():
#     # pass_var.append('dest value')
#     # pass_var = ['dest value']
#     pass_var[1] = 'dest value'
#     print(pass_var)
#
#
# pass_var = ['source value']
# print(pass_var)
# show_text()
# print(pass_var)

# return None
print(print())
x = None

if x is None:
    print('None')


def greet(name):
    print('Hello, ', name, '!', sep='')


print(greet('SPK'))

# return values