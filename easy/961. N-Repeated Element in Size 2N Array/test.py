# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
from collections import Counter

def isRepeated(A):
    # b = Counter(A[:])
    # return b.most_common()[0][0]
    alist = []
    for i in A:
        if i not in alist:
            alist.append(i)
        else:
            return i


A = [1,2,3,3]
B = [2,1,2,5,3,2]
C = [5,1,5,2,5,3,5,4]

print(isRepeated(C))


# for(int i = 0; i<A.length;i++){
#     if(!list.contains(A[i]))
#         list.add(A[i]);
#     else
#         return A[i];
# }