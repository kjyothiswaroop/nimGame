#!/usr/bin/env python3
import board

class nimGame:

    def __init__(self):
        self.players = 0
        self.rows = 0
        self.count = []
        self.board_obj = []

    # Function to take input and setup the game
    def userInput(self):
        print("Welcome to the Nim Game!")

        print("Let's begin with setting up the board.")
        print("Please enter the number of rows:")
        self.rows = int(input())
        self.count = [0] * self.rows
        for i in range(self.rows):
            print(f"For row {i+1}, how many sticks would you like?")
            self.count[i] = int(input())
        print("Please enter the number of players :")
        self.players = int(input())
        return self.players,self.rows,self.count

    # Function to recursively play the game and display the board and finally the winner
    def game(self,board):
        current_player = 0
        while True:
            sticks_left = sum(row.count('|') for row in self.board_obj)
            if sticks_left == 1:
                print(f"Player {(current_player + 1) % self.players + 1} wins!")
                break

            print(f"Player {current_player + 1}'s turn:")
            rows = len(self.board_obj)
            while True:
                print(f"Choose the row to remove sticks from between 1 and {rows}:")
                removeRow = int(input())
                if removeRow < 1 or removeRow > rows or self.board_obj[removeRow - 1].count('|') == 0:
                    print("Invalid row number or no sticks left in this row. Try again.")
                    continue
                while True:
                    max_sticks = self.board_obj[removeRow - 1].count('|')
                    print(f"How many sticks do you want to remove between 1 and {max_sticks}?")
                    removeCount = int(input())
                    if removeCount < 1 or removeCount > max_sticks:
                        print("Invalid stick count. Try again.")
                        continue
                    break
                self.board_obj = board.updateBoard(removeRow - 1, removeCount)
                board.displayBoard()
                break

            current_player = (current_player + 1) % self.players

# Main Function
def main():
    gamePlay = nimGame()
    inputResult = gamePlay.userInput()
    result = board.Board(inputResult[1], inputResult[2])
    gamePlay.board_obj = result.board
    result.displayBoard()
    gamePlay.game(result)
    
if __name__ == "__main__":
    main()