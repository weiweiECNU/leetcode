alist = [1,2,3,4,6,5,7,8,9]
# print(alist[:index]+alist[index+1:] )
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for index in range(len(nums)):
            blist = nums[:index]+nums[index+1:] 
            if all( blist[x]<= blist[x+1] for x in range(len(blist)-1)):
                return True

        return False


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1,len(nums)):
            if nums[i]< nums[i - 1]:
                count += 1
                if i == 1 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]


        return count <= 1