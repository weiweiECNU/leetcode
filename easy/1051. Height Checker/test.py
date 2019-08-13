# https://leetcode.com/problems/height-checker/
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        type height : List[int]
        rtype : int
        """
        right = sorted( heights )
        result = 0
        for i in range(len(heights)):
            if right[i] != heights[i]:
                result += 1
            
        return result