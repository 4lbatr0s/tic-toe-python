import random


def display_board(board):
    print(
    '        |       |       \n'
    '    {6}   |    {7}  |    {8}  \n'
    '        |       |       \n'
    '----------------------------\n'
    '        |       |       \n'
    '    {3}   |    {4}  |    {5}  \n'
    '        |       |       \n'
    '----------------------------\n'
    '        |       |       \n'
    '    {0}   |    {1}  |    {2}  \n'
    '        |       |       \n'.format(board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9])

)


def player_input():
    while(True):
        input_value = input('Enter a value:')
        input_value = input_value.upper()
        if(input_value == 'X' or input_value =='O'):
            return input_value
        else:
            print('Sorry, enter a valid value')


def assign_position():
        position = int(input('Occupy a position:'))
        return position


def place_marker(board,position,marker):
        board[position] = marker


def win_check(board, mark):
    if ((board[1] == board[2] == board[3] == mark) 
    or (board[4] == board[5] == board[6] == mark) 
    or (board[7] == board[8] == board[9] == mark)
    or (board[1] == board[4] == board[9] == mark)
    or (board[7] == board[4] == board[3] == mark)):
        return True
    


def choose_first():
    starter = random.randint(1,2)
    return starter

def space_check(board, position):
    if(board[position] == ''):
        return True
    else:
        return False

def full_board_check(board):
    for i in board:
        if(i !=''):
            return True
        else:
            return False


def clear_board(board):
    for i in board:
        board[i] = ''
    return board

def clear_or_not():
    clear_the_board = input('Do you want us to clear the board? (y/n) or (Y/N):')
    clear_the_board = clear_the_board.lower()
    if(clear_the_board == 'y'):
        return True
    elif(clear_the_board =='n'):
        return False

def player_choice(board):
    next_position = int(input('Player\'s nex position (1-9):'))
    space_check(board, next_position)

def replay():
    wish = input('Would you like to play again? (y/n) or (Y/N):')
    wish = wish.lower()
    if(wish == 'y'):
        return True
    elif(wish == 'n'):
        return False

board = ['#','','','','','','','','','']
print('Welcome to the TIC-TAC-TOE game!, Enjoy..')
while True:
    display_board(board)
    first_goes = choose_first()
    if(first_goes == 1):
        player = 'First Player'
    else:
        player = 'Second Player'
    
    input_value = player_input()
    position = assign_position()
    if(space_check(board, position)):
        place_marker(board,position, input_value)
        display_board(board)
        if(win_check(board, 'X')):
            print('{} has won the game'.format('x'))
            if(replay()):
                continue
            else:
                print('Game Over')
                break
        elif(win_check(board, 'O')):
            print('{} has won the game'.format('O'))
            if(replay()):
                continue
            else:
                print('Game  Over.')
                break
        if(full_board_check(board)):
            if(clear_or_not()):
                clear_board(board)
                display_board(board)
        else:
            continue





        




