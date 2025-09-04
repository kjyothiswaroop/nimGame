#!/usr/bin/env python3

def constructBoard(rows,count):
    board = [''] * rows
    for i in range (rows):
        board[i] = '|' * count[i]
    return board

def displayBoard(board):
    for row in board:
        print(row)

def updateBoard(board,removeRow,removeCount):
    board[removeRow] = '|' * max(0, board[removeRow].count('|') - removeCount)
    return board


if __name__ == "__main__":
    pass