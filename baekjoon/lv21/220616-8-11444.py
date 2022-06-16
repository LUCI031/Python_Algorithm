import sys
input=sys.stdin.readline
p = 1000000007
def pow(adj,n):
    if n == 1:
        return adj
    elif n%2:
        return mul(pow(adj,n-1),adj)
    else:
        return pow(mul(adj,adj),n//2)

def mul(a,b):
    tmp = [[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k] * b[k][j]
            tmp[i][j] = sum%p
    return tmp

adj = [[1,1],[1,0]]

start = [[1],[1]]
n = int(input())

if n < 3:
    print(1)

else:
    print(mul(pow(adj,n-2),start)[0][0])