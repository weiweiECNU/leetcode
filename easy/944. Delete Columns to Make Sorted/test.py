A = ["cba","daf","ghi"]
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        width = len(A[0])
    
        for index in range(width):
            alist = [string[index] for string in A ]
            if all(alist[i] <= alist[i+1] for i in range(len(alist)-1)):
                width -= 1
        
        return width