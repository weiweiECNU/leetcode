# https://leetcode.com/problems/fibonacci-number/


class Solution:
    def fib(self, N: int) -> int:
        """
        基本结束条件 : num == 2
        演进: 前两项之和
        """
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib( N-1) + self.fib(N - 2)

