#https://leetcode.com/problems/jewels-and-stones/
J = "aA"
S = "aAAbbbb"

def numJewelsInStones(self, J: str, S: str) -> int:
    number = 0
    for jewel in J:
        for stone in S:
            if stone == jewel:
                number += 1
    return number