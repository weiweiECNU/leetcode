class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position = [0,0]
        for letter in moves:
            if letter == "R":
                position[0] += 1
            if letter == "L":
                position[0] -= 1
            if letter == "U":
                position[1] += 1
            if letter == "D":
                position[1] -= 1
                
        return position == [0,0]

# @Asthestarsfall

# def judgeCircle(self, moves: str) -> bool:

#     if not moves:
#         return True
    
#     cnt = collections.Counter(moves)
    
#     if cnt['U'] != cnt['D'] or cnt['L'] != cnt['R']:
#         return False        
#     return True