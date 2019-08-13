# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        """
        type A: List[int]
        rtype : List[int]
        """
        odd = [x for x in A if x % 2 == 1]
        even = [x for x in A if x % 2 == 0]

        result = []
        for i in range(len(odd)):
            result.append(even[i])
            result.append(odd[i])
        
        return result

        # j = 1
        # for i in range(0,len(A),2):
        #     if A[i] % 2 == 0: 
        #         continue
        #     while A[j] % 2 != 0: 
        #         j += 2
        #     A[i], A[j] = A[j], A[i]
        # return A


        # 先对A进行排序，使得偶数都在前面，奇数都在后面，
        # A.sort(key = lambda x : x % 2)
        # N = len(A)
        # res = []
        # for i in range(N // 2):
        #     res.append(A[i])
        #     res.append(A[N - 1 - i])
        # return res