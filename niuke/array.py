"""
小红有两个长度为n的排列A和B。每个排列由[1,n]数组成，且里面的数字都是不同的。

现在要找到一个新的序列C，要求这个新序列中任意两个位置(i,j)满足:

如果在A数组中C[i]这个数在C[j]的后面，那么在B数组中需要C[i]这个数在C[j]的前面。

请问C序列的长度最长为多少呢？


输入描述:
第一行一个整数，表示N。

第二行N个整数，表示A序列。

第三行N个整数，表示B序列。

满足:N<=50000

输出描述:
输出最大的长度

输入例子1:
5
1 2 4 3 5
5 2 3 4 1

输出例子1:
4

例子说明1:
最长的C为1,3,4,5
"""
def isLeft(x,y,alist):
    return alist.index(x) < alist.index(y)

def isRight(x,y,alist):
    return alist.index(x) > alist.index(y)


def presence( x,y,alist, blist):
    return isLeft(x,y,alist) ^ isRight(x,y,blist)

n = map(int, input().split())

a = []
for i in map(int, input().split()):
    a.append(i)

b = []
for i in map(int, input().split()):
    b.append(i)

c = []

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self, neighborId,weight):
        self.connectedTo[neighborId] = weight
    

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, id):
        newVertex = Vertex(id)
        self.vertList[id] = newVertex
        self.numVertices += 1
        return newVertex

    def addEdge(self, id1, id2, weight = 1):
        if id1 not in self.vertList:
            vertex1 = self.addVertex(id1)
        if id2 not in self.vertList:
            vertex2 = self.addVertex(id2)
        self.vertList[id1].addNeighbor(self.vertList[id2], weight)    #单向图
    
    def isEdge(self, id1, id2):
        alist = []
        for w in self.vertList[id1].getConnections():
            alist.append(w.getId())
        return id2 in alist

    def __iter__(self):
        return iter(self.vertList.values()) # 返回字典中的所有值。 values()
g = Graph()

for i in range(1, n+1):
    for j in range(1,n+1):
        if presence(i,j,a,b) == False:
            g.addEdge(i,j,1)

# 最大团问题


# for i in range(1, n+1):
#     flag = True
#     for j in range(1,n+1):
#         if presence(i,j,a,b) != False:
#             flag = False

#     if flag == True:
#         c.append(i)

