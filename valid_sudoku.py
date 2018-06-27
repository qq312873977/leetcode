"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #row detect
        col_num = 9
        for row in board:
            nums = []
            for ch in row:
                if ch != '.':
                    nums.append(ch)
            if len(nums) != len(set(nums)):
                return False

        #column detect
        for col in range(col_num):
            nums = []
            for row in range(col_num):
                if board[row][col] != '.':
                    nums.append(board[row][col])
            if len(nums) != len(set(nums)):
                return False

        #nine small board
        for row in range(0, col_num, 3):
            for col in range(0, col_num, 3):
                nums = []
                for i in range(3):
                    for j in range(3):
                        if board[row+i][col+j] != '.':
                            nums.append(board[row+i][col+j])
                if len(nums) != len(set(nums)):
                    return False

        return True
