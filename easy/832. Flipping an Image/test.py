# https://leetcode.com/problems/flipping-an-image/

# 
class Solution:
    def flip(self, A: List) -> List:
        fliped = []
        for index in range( len(A)-1,-1, -1):
            fliped.append(A[index])
        return fliped

    def invert(self, A: List) -> List:
        inverted = []
        for index in range(len(A)):
            inverted.append( abs( A[index] - 1) )
        
        return inverted
    
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for i, row in enumerate(A):
            a = self.flip(row)
            b = self.invert(a)
            result.append(b)
        return result