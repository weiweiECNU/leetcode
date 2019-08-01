"""
现在有q个询问，每次询问想问你在[l,r]区间内，k进制表示中，k-1的数量最多的数是哪个数。比如当k=2时，9的二进制就是1001，那么他就有2个1.


输入描述:
第一行一个q，表示有q组询问。

接下来q行，每行三个整数k,l,r,分别表示进制数,查询的数字,以及查询的范围。

满足1<=q<=100000,2<=k<=16,1<=l<=r<=10^16

输出描述:
对于每组询问，输出答案。如果有多个答案，请输出最小的。

输入例子1:
1
8 1 100

输出例子1:
63

"""
import math
import numpy as np

n = int(input())
min = 0 
for i in range(n):
    k,l,r = map(int, input().split())
    


def maxDigits(k,l,r):
    mins = int(math.log(l,k)) + 1
    maxs = int(math.log(r,k)) + 1


def isin(num, l , r):
    return  num >= l and num <= r 


case = []
for i in range(maxs-1,-1,-1):
    case.append( (k-1) ** i )

case = np.matrix(case).T


digits = []
for i in range(maxs,mins-1,-1):
    
    case.append()


print(num)
