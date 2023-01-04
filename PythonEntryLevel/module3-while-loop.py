# counter = 1
# print('Loop Started...')
# while counter < 11:
#     print(counter)
#     counter += 1
# print('Loop Ended!')

# Guess game
secret_number = 10
input_number = 1
attempts = 5

print('''
###################################
##### THE SECRET NUMBER GAME ######
###################################
''')

while secret_number != input_number and attempts > 0:
    input_string = 'Guess the secret number (Range 1-20, Remaining attempts', attempts, ') : '
    input_number = int(input(input_string))
    attempts -= 1
if attempts == 0:
    print('Attempts exceeded!')
else:
    print('That\'s correct!')
