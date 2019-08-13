# https://leetcode.com/problems/di-string-match/
"""
题目大意
已知一个字符串只包含I和D，求[0～N]的一个排列，使得如果字符串的某个位置是I，那么数组对应的位置和后面的位置是递增的；如果字符串的某个位置是D，那么数组对应的位置和后面的位置是递减的。

解题方法
乍一看很难的题目，但是仔细分析一下，发现很简单的：类似于贪心策略，我们使第一个出现的I的位置对应的是0，第一个D出现的位置对应的是N，那么无论这个位置后面无论出现的是另外的哪个数字，当前的位置都能满足题设条件。我们每次遇见I都比之前的I增加1，每次遇到D都比之前的D减小1.这样会尽可能的给后面的数字让出空间。

最后还要注意的是数组比字符串多一个位置，这个位置其实就是剩下的那个数字，比如我的解法中的ni或者nd都可以。

时间复杂度是O(N)，空间复杂度是O(1)。

class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N = len(S)
        ni, nd = 0, N
        res = []
        for s in S:
            if s == "I":
                res.append(ni)
                ni += 1
            else:
                res.append(nd)
                nd -= 1
        res.append(ni)
        return res
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
日期
2018 年 11 月 18 日 —— 出去玩了一天，腿都要废了


--------------------- 
版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循CC 4.0 by-sa版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/84206493
"""

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        """
        type S: str
        rtype : List[int]
        """
        l = 0
        h = len(S) 
        out = []
        for i in S:
            if i == "I":
                out.append(l)
                l += 1
            elif i == "D":
                out.append(h)
                h -= 1
        
        out.append(h)
        return out