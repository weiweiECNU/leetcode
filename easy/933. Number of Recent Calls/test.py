# https://leetcode.com/problems/number-of-recent-calls/
# 双向队列
class RecentCounter:

    def __init__(self):
        self.queue = []
        self.size = 0
        

    def ping(self, t: int) -> int:
        """
        :type t : int
        :rtype : int
        """
        for index in range(len(self.queue)):
            if self.queue[0] < t - 3000:
                self.queue.pop(0)
                self.size -= 1
            else:
                break
                
        
        self.queue.append(t)
        self.size += 1
        return self.size
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)