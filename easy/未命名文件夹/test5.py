import sys 
a = sys.stdin.readline().strip().split()
N = int(a[0])
K = int(a[1])
string = sys.stdin.readline().strip()

buffer = [0]* (K-1)
result = ""
for i in range(N):
    buffer_result = sum(buffer) % 2
    num = abs(buffer_result - int(string[i]))
    buffer.insert(0,num)
    buffer.pop()
    result += str(num)
    
print(result)
    
