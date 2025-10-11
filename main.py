def print_board():
    for row in board:
        print(' +---+---+---+')
        out = ' | ' + ' | '.join(row) + ' |'
        print(out)
    print(' +---+---+---+')

def is_full():
    for row in board:
        if row.count(' ') > 0:
            return False
    return True

def winner():
    global who_won, board
    '''
    There are 8 possible winning combination on the tictactoe board.
    1. 0-0, 0-1, 0-2  
    2. 1-0, 1-1, 1-2
    3. 2-0, 2-1, 2-2
    4. 0-0, 1-0, 2-0 
    5. 0-1, 1-1, 2-1
    6. 0-2, 2-1, 2-2
    7. 0-0, 1-1, 2-2 
    8. 0-2, 1-1, 2-0
    '''
    possible = [
        [[0,0], [0,1], [0,2]],
        [[1,0], [1,1], [1,2]],
        [[2,0], [2,1], [2,2]],
        [[0,0], [1,0], [2,0]],
        [[0,1], [1,1], [2,1]],
        [[0,2], [1, 2], [2,2]],
        [[0,0], [1,1], [2,2]],
        [[0,2], [1,1], [2,0]]
    ]
    for match in possible:
        init = board[match[0][0]][match[0][1]]
        if init == ' ':
            continue
        winner = True
        for r,c in match:
            if board[r][c] != init:
                winner = False
                break
        if winner:
            who_won = init
            return True
    return False
    

def game_ended():
    return is_full() or winner()


while True:
    board = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]
    who_won = None
    print_board()
    turn = 0
    while not game_ended():
        move = input('Row-Col: ')
        try:
            row, col = map(lambda x: int(x) - 1, move.split('-'))
        except ValueError:
            print("Wrong input format. Use Row-Col format (e.g., 1-3 for Row 1 Column 3)")
            continue
        char = ['X', 'O'][turn]
        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == ' ':
                board[row][col] = char

                turn = (turn + 1) % 2
                print_board()
            else:
                print('Place is already taken')
        else:
            print("Row and column must be within 1 to 3")
    else:
        if who_won != None:
            print('Winner:', who_won)
        else:
            print('Board is full')

    cmd = input("Enter 'R' to restart and 'C' to close the game.\n")
    while not (cmd == 'C' or cmd == 'R'):
        cmd = input("Wrong command.\nEnter 'R' to restart and 'C' to close the game.\n")
    if cmd == 'C':
        break
