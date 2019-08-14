# https://leetcode.com/problems/subdomain-visit-count/
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        wordDict = {}
        for i in cpdomains:
            aList = i.replace("."," ").split()
            number = int(aList[0])
            for i in range(len(aList)-1,0,-1):
                word = ".".join(aList[i:])
                if word not in wordDict:
                    wordDict[word] = 0
                wordDict[word] += number

        return [str(wordDict[i])+" "+i for i in wordDict]
        