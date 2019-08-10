# https://leetcode.com/problems/self-dividing-numbers/
#For each number in the range, check whether it is self dividing by converting that number to a character array (or string in Python), 
# then checking that each digit is nonzero and divides the original number.
# 考虑用递归

import math

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        alist = []
        for number in range(left, right+1):
            if self._selfDivided(number):
                alist.append(number)
        
        return alist
    
    def _selfDivided(self, num):
        digits = int(math.log10(num)) + 1
        for index in range(digits):
            digit = int(str(num)[index])
            if digit == 0:
                return False
            elif num % digit  != 0:
                return False
        
        return True