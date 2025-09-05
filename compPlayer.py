#!/usr/bin/env python3
import board

class computerPlayer:
    def __init__(self,bo):
        self.nimSum : int
        self.obj = bo

    def nimSum(self,board):
        for i in range(len(board)):
            self.nimSum ^= board[i].count('|')

    def checkforOddOnes(self,board):
        heapSizes = [row.count('|') for row in board if row.count('|') > 0]
        if (all(size == 1 for size in heapSizes) and len(heapSizes)%2 == 1):
            return True
        return False
    
    def optimalMove(self,board_obj):
        heap_sizes = [row.count('|') for row in board_obj]
        non_empty_heaps = [size for size in heap_sizes if size > 0]
        #make a move such that nimSum always equates to zero given that you are not leaving the opponent with an even number of 1's in each heap
        if(self.checkforOddOnes(board_obj)):
            for i, row in enumerate(board_obj):
                if row.count('|') == 1:
                    self.obj.updateBoard(i, 1)
                    print(f"Computer removes 1 stick from row {i+1}")
                    return
        elif all(size == 1 for size in non_empty_heaps):
                if row.count('|') == 1:
                    self.obj.updateBoard(i, 1)
                    print(f"Computer removes 1 stick from row {i+1}")
                    return
        else :
            nim_sum = 0
            for size in non_empty_heaps:
                nim_sum ^= size

            # Find a heap to reduce to make Nim-sum 0
            for i, size in enumerate(non_empty_heaps):
                target_size = size ^ nim_sum
                if target_size < size:
                    remove_count = size - target_size
                    # Update the actual board row
                    for j, row in enumerate(board_obj):
                        if row.count('|') == size:
                            self.obj.updateBoard(j, remove_count)
                            print(f"Computer removes {remove_count} stick(s) from row {j+1}")
                            return
                        
        for i, row in enumerate(board_obj):
            if row.count('|') > 0:
                self.obj.updateBoard(i, 1)
                print(f"Computer removes 1 stick from row {i+1}")
                return

if __name__ == "__main__":
    pass