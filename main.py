#!/usr/bin/env python3
import board

def userInput():
    print("Welcome to the Nim Game!")

    print("Let's begin with setting up the board.")
    print("Please enter the number of rows:")
    rows = int(input())
    count = [0] * rows
    for i in range(rows):
        print(f"For row {i+1}, how many sticks would you like?")
        count[i] = int(input())
    print("Please enter the number of players :")
    players = int(input())
    return players,rows,count

def game(players, board_obj):
    current_player = 0
    while True:
        sticks_left = sum(row.count('|') for row in board_obj)
        if sticks_left == 1:
            print(f"Player {(current_player + 1) % players + 1} wins!")
            break

        print(f"Player {current_player + 1}'s turn:")
        rows = len(board_obj)
        while True:
            print(f"Choose the row to remove sticks from between 1 and {rows}:")
            removeRow = int(input())
            if removeRow < 1 or removeRow > rows or board_obj[removeRow - 1].count('|') == 0:
                print("Invalid row number or no sticks left in this row. Try again.")
                continue
            while True:
                max_sticks = board_obj[removeRow - 1].count('|')
                print(f"How many sticks do you want to remove between 1 and {max_sticks}?")
                removeCount = int(input())
                if removeCount < 1 or removeCount > max_sticks:
                    print("Invalid stick count. Try again.")
                    continue
                break
            board_obj = board.updateBoard(board_obj, removeRow - 1, removeCount)
            board.displayBoard(board_obj)
            break

        current_player = (current_player + 1) % players
        

def main():
    inputResult = userInput()
    result =  board.constructBoard(inputResult[1],inputResult[2])
    board.displayBoard(result)
    game(inputResult[0],result)

   
if __name__ == "__main__":
    main()