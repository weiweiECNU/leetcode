"""
有一个城市需要修建，给你N个民居的坐标X,Y，问把这么多民居全都包进城市的话，城市所需最小面积是多少（注意，城市为平行于坐标轴的正方形）


输入描述:
第一行为N，表示民居数目（2≤N≤1000）

输出描述:
城市所需最小面积

输入例子1:
2
0 0
2 2

输出例子1:
4

输入例子2:
2
0 0
0 3

输出例子2:
9
"""


n = int(input())

for i in range(n):
    x,y =  map(int, input().split())
    if i == 0:
        xLargest = x
        xSmall = x
        yLargest = y
        ySmall = y
    else:
        if x > xLargest:
            xLargest = x
        if x < xSmall:
            xSmall = x
        if y > yLargest:
            yLargest = y
        if y < ySmall:
            ySmall = y

xLength = xLargest-xSmall
yLength = yLargest-ySmall


if xLength > yLength:
    print(xLength ** 2 )
else:
    print(yLength ** 2)
