#!/usr/bin/env python3

class Board :
    def __init__(self,rows,count):
        self.rows = rows
        self.board = [''] * rows
        for i in range (rows):
            self.board[i] = '|' * count[i]

    def displayBoard(self):
        for row in self.board:
            print(row)

    def updateBoard(self,removeRow,removeCount):
        self.board[removeRow] = '|' * max(0, self.board[removeRow].count('|') - removeCount)
        return self.board

if __name__ == "__main__":
    pass