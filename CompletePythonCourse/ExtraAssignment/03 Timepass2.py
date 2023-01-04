# # heads or tails
# import random
# result = random.randint(0,1)
# if result == 0:
#     print('Heads')
# else:
#     print('Tails')

# united_states = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland',
#              'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont',
#              'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine',
#              'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota',
#              'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota',
#              'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska',
#              'Hawaii']

# # who pays the bill, pick random person in a list
# import random
# names_string = 'SPK, PSK, SPK1, NSK, SSK'
# names = names_string.split(', ')
# random_index = random.randint(0, len(names) - 1)
# print(f'{names[random_index]} is going to buy the meal today!')

# # Rock, Paper, Scissors
# import random
#
# scissors = '''
#     _______
# ---'   ____)_____
#           _______)
#        ___________)
#       (____)
# ---.__(___)
# '''
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# papers = '''
#     _______
# ---'   ____)______
#           ________)
#           _________)
#          _________)
# ---.____________)
# '''
#
# rock_paper_scissors = [rock, papers, scissors]
#
# print('### Rock Paper Scissors ###')
# user_input = int(input('What do you choose? Type 0 for "Rock", 1 for "Paper", 2 for "Scissors": '))
# print(f'Your choice: {rock_paper_scissors[user_input]}')
# computer_input = random.randint(0, 2)
# print(f'Computer\'s choice: {rock_paper_scissors[computer_input]}')
#
# if user_input == computer_input:
#     print('IT\'S DRAW!')
# elif computer_input == 0 and user_input == 2:
#     print('COMPUTER WINS!')
# elif computer_input == 2 and user_input == 0:
#     print('USER WINS!')
# elif user_input > computer_input:
#     print('USER WINS!')
# elif computer_input > user_input:
#     print('COMPUTER WINS!')

# # Password Generator Project
#
# import random
#
# letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
#           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print('Welcome to the PyPassword Generator')
# print('Password should contain how many')
# nr_letters = int(input('letters: '))
# nr_symbols = int(input('symbols: '))
# nr_numbers = int(input('numbers: '))
#
# password = ['']
# for nr in range(nr_letters):
#     password.append(letter[random.randrange(0, len(letter))])
#
# for nr in range(nr_symbols):
#     password.append(symbols[random.randrange(0, len(symbols))])
#
# for nr in range(nr_numbers):
#     password.append(numbers[random.randrange(0, len(numbers))])
#
# password.remove('')
# random.shuffle(password)
# password = ''.join(password)
# print(f'Generated {password} of length {len(password)}')

