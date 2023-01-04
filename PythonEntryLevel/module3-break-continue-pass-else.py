# # Guess game
# secret_number = 10
# input_number = 1
# attempts = 5
#
# print('''
# ###################################
# ##### THE SECRET NUMBER GAME ######
# ###################################
# ''')
#
# while True:
#     print(attempts, 'attempts remaining!')
#     input_number = int(input('Guess the secret number (Range 1-20) : '))
#     attempts -= 1
#     if input_number != secret_number and attempts > 0:
#         continue
#     break
#
# if attempts == 0:
#     print('XXX Attempts Exceeded! XXX')
# else:
#     print('THAT\'s CORRECT!')

# # Prime number
# print('---', end='')
# while True:
#     print('---')
#     input_number = int(input('Enter number: '))
#     prime = False
#
#     if input_number <= 1:
#         pass
#     elif input_number == 2 or input_number == 3:
#         prime = True
#     else:
#         prime = True
#         for number in range(2, int(input_number / 2) + 1):
#             if input_number % number == 0:
#                 prime = False
#                 break
#     print('---')
#     if prime:
#         print(input_number, 'IS a Prime number')
#     else:
#         print(input_number, 'IS NOT a Prime number')
#     print('---')
#     if input('Do you want to one more number [y,n]? ') == 'y':
#         continue
#     else:
#         print('------')
#         break

# Nested loop:
for i in range(1,5):
    for j in range(1,11):
        print(i, 'X', j, '=', i * j)
    print('---')
else:
    print('End of loop', j)