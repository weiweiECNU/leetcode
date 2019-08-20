# https://leetcode.com/problems/projection-area-of-3d-shapes/

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return self.fromSide(grid) + self.fromTop(grid) + self.fromFront(grid)

    def fromTop(self, grid):
        return sum([1 for k in grid for i in k if i > 0] )
    
    def fromFront(self,grid):
        number = 0
        for x in grid:
            number += max(x)
            
        return number
    
    def fromSide(self, grid):
        number = 0

        for col in range(len(grid)):
            number += max([ grid[i][col] for i in range(len(grid)) ])
        return number
                