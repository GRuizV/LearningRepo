def print_board(board):

    print('-------------')

    for i in range(3):
        print('|', board[i][0], '|', board[i][1], '|', board[i][2], '|')

        print('-------------')


def check_win(board):

    for i in range(3):

        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        
        elif board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
        
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    
    elif board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    
    return False


def tic_tac_toe():

    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player = 'X'

    while True:

        print_board(board)

        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter column (0-2): "))

        if board[row][col] == ' ':

            board[row][col] = player

            if check_win(board):

                print_board(board)

                print(f"Player {player} wins!")
                break

            if player == 'X':
                player = 'O'
                
            else:
                player = 'X'

        else:
            print("That spot is already taken. Try again.")


tic_tac_toe()