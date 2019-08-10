# https://leetcode.com/problems/array-partition-i/
# 比较大的数字一定要和比较大的数字在一起才行，否则括号内的小的结果是较小的数字。
# 所以先排序，排序后的结果找每个组中数据的第一个数字即可。
# 时间复杂度是O(NlogN)，空间复杂度是O(1).
    
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])