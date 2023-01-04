board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]

symbol_mapping = {}
symbol_list = ['X', 'O']
winning_position_lists = [[1, 2, 3], [1, 5, 9], [1, 4, 7], [2, 5, 8], [4, 5, 6], [3, 5, 7], [7, 8, 9]]


def print_board():
    print(' ---status---')
    for index in range(9):
        if index == 0 or index == 3 or index == 6:
            print('|  ', end='')
        print(board[index], end='  ')
        if index == 2 or index == 5 or index == 8:
            print('|')
    print(' -----------')


def validate_and_place(position, symbol):
    if symbol not in symbol_list:
        print('ERROR: Invalid symbol ' + symbol + '. Valid symbols: ' + symbol_list[0] + ' and ' + symbol_list[1] + '.')
        return False
    if board[position-1] != '-':
        print('ERROR: Position ' + str(position) + ' already occupied.')
        return False
    board[position-1] = symbol
    print('Placed ' + symbol + ' at ' + str(position) + '.')
    return True


def input_from_user(player_name):
    input_position = input('Enter position for ' + player_name + ' (1-9): ')
    if input_position.isnumeric() and 0 <= int(input_position) < 10:
        return int(input_position)
    else:
        print('ERROR: Invalid position ' + input_position + '. Valid range (1-9).')
        return input_from_user(player_name)


def check_for_result():
    for winning_list in winning_position_lists:
        if board[winning_list[0]-1] == board[winning_list[1]-1] == board[winning_list[2]-1]\
                and board[winning_list[0]-1] != '-' \
                and board[winning_list[1]-1] != '-' \
                and board[winning_list[2]-1] != '-':
            print_board()
            print(" ******** THE WINNER IS " + players[player_index] + "! CONGRATULATIONS!!! ********")
            return True
    if '-' not in board:
        print_board()
        print(" ******** IT\'s A DRAW!!! ********")
        return True
    return False


def how_to_play():
    title = '''
    ####### # #####    #######     #     #####    ####### ####### #######  
       #    # #           #       # #    #           #    #     # #
       #    # #           #      #___#   #           #    #     # ######
       #    # #           #     #-----#  #           #    #     # #
       #    # #####       #    #       # #####       #    ####### #######
    '''
    print(title)
    print("Rules")
    print('1. Two player game, one by one will get chance to place symbol.')
    print('2. Player need to enter position where to place it\'s symbol')
    print('3. If you wanna quit, Enter position as 0 (Zero)')
    print('4. If something seems wrong, look for warning')
    input_player_names()


def input_player_names():
    print('Enter player names (max 15 length)')
    player_in_1 = input('Player1: ')
    player_in_2 = input('Player2: ')
    if player_in_1 == player_in_2 or len(player_in_1) > 15 or len(player_in_2) > 15:
        print('ERROR: EITHER Name length should be less 15 OR Names should be different!')
        input_player_names()
    symbol_mapping[player_in_1] = 'X'
    symbol_mapping[player_in_2] = 'O'


def wanna_play_again():
    wanna_play_in = input('Wanna play again? (y/n): ')
    if wanna_play_in != 'y' or wanna_play_in != 'n':
        print('Invalid input!')
        return wanna_play_again()
    if wanna_play_in == 'y':
        how_to_play()
        print_board()
        return True
    return False


how_to_play()
players = list(symbol_mapping.keys())
player_index = 1
print_board()

while True:
    # Select player turn
    if player_index == 0:
        player_index = 1
    else:
        player_index = 0
    # Take input position and place symbol in position (keep doing unless position input is valid)
    while True:
        user_input = input_from_user(players[player_index])
        if user_input == 0:
            print('Input received 0... Good Bye!!')
            exit(0)
        if validate_and_place(user_input, symbol_mapping[players[player_index]]):
            break
    # Check result
    game_finished = check_for_result()
    if game_finished:
        wanna_play= wanna_play_again()
        if not wanna_play:
            break
        player_index = 1
