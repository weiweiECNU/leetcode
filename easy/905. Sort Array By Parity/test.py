class Solution:
    def sortArrayByParity(self, A):
        even = []
        odd = []
        for number in A:
            if number % 2 == 0:
                even.append(number)
            else:
                odd.append(number)
        
        return even+odd




# 3shine
class Solution(object):
    def sortArrayByParity(self, A):
        A.sort(key = lambda x: x%2==1)
        return A