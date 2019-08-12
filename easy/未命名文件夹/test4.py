import sys
n = int(sys.stdin.readline().strip())
clock = []
for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        clock.append(values)


road = int(sys.stdin.readline().strip())
finish = list(map(int, sys.stdin.readline().strip().split()))

def clock2time(clock):
    return clock[0]*60 + clock[1]

finish = clock2time(finish)
start = finish - road

clock = sorted(clock,reverse = True) 
def findClock(clock, start):
    for i in range(0, len(clock), 1):
        clock_i = clock2time(clock[i])
        if clock_i <= start:
            return clock[i]


find = findClock(clock, start)
print(find[0],find[1])
