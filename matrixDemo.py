#Sam Krimmel
#4/27/18
#matrixDemo.py - using lists, but better, listception

def printBoard(board):
    for r in range(0,3):
        for c in range(0,3):
            print(board[r][c],end=' ')

board = [['a','b','c'],['d','e','f'],['g','h','i']]

printBoard(board)
