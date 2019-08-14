# https://leetcode.com/problems/relative-sort-array/

# 用的 freq dict 


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {x:0 for x in arr2}
        reserve = []
        for i in arr1:
            if i in freq:
                freq[i] += 1
            else:
                reserve.append(i)
        
        reserve.sort()
        
        left = []
        for i in freq:
            for j in range(freq[i]):
                left.append(i)
        
        return left + reserve
            
            
  
