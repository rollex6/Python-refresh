# Tic-Tac-Toe Game

board = [' ' for x in range(10)]

def insertLetter (letter, position):
    board[position] = letter

def spaceIsFree(position):
    return board[position] === ' '

def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def isBoardFull(board):
    if board.count(' ' > 1):
        return False
    else:
        return True

def winner(b,l):
    return (b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == 1) or
    (b[2] == l and b[5] == l and b[8] == 1) or
    (b[3] == l and b[6] == l and b[9] == 1) or
    (b[1] == l and b[5] == l and b[9] == 1) or
    (b[3] == l and b[5] == l and b[7] == 1)

def playerMove():
    run = True
    while run:
        move = input('Please enter a position to play from 1 - 9')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('Please type a number that is valid from 1 - 9')

        except:
            print('Please type a valid number')

def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[:] = let
            if winner(boardcopy, let):
                move = i
                return move
                