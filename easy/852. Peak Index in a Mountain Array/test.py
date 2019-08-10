# https://leetcode.com/problems/peak-index-in-a-mountain-array/

def peakIndexInMountainArray( A ):
    left = 0
    right = len(A) - 1
    leftvalue = -1
    rightvalue = -1
    mid = -1
    
    while(left <= right):
        mid = (right + left)//2
        leftvalue = A[mid-1] if mid - 1 >= 0 else 0
        rightvalue = A[mid+1] if mid + 1 <= len(A)-1 else A[len(A)-1]
        
        print(mid)
        print(leftvalue)
        print(rightvalue)
        
        if A[mid] > leftvalue and A[mid] > rightvalue:
            return mid
        elif A[mid] <= rightvalue:
            left = mid+1
        else:
            right = mid-1
        
        print(mid, left, right)
        print()
    
    return -1


A = [3,4,5,1]
peakIndexInMountainArray(A)