# https://leetcode.com/problems/available-captures-for-rook/
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        (row, column) = self.findRook(board)
        number = 0
        # left
        for i in range(column-1,-1,-1):
            if board[row][i] == "B":
                break
            elif board[row][i] == "p":
                number += 1
                break
        # right 
        for i in range(column+1,8):
            if board[row][i] == "B":
                break
            elif board[row][i] == "p":
                number += 1
                break
                
#         # up
        for i in range(row-1,-1,-1):
            if board[i][column] == "B":
                break
            elif board[i][column] == "p":
                number += 1
                break
#         # down
        for i in range(row+1,8):
            if board[i][column] == "B":
                break
            elif board[i][column] == "p":
                number += 1       
                break
        return number
                
        
    
    def findRook(self, board):
        for i, row in enumerate(board):
            for j, chess in enumerate(row):
                if chess == "R":
                    return (i,j)

                