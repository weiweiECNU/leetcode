# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        digits = max(len(x_bin), len(y_bin))
        if len(x_bin) > len(y_bin):
            y_bin = "0"*(len(x_bin)-len(y_bin)) + y_bin
        elif len(x_bin) < len(y_bin):
            x_bin = "0"*(len(y_bin)-len(x_bin)) + x_bin
        
        distance = 0
        for digit in range(digits):
            distance += abs( int(x_bin[digit]) - int(y_bin[digit]) )
        
        return distance 