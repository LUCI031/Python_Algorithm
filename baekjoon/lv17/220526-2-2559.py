import sys
input=sys.stdin.readline

N,M = map(int, input().split())

lst = list(map(int, input().split()))
c= [sum(lst[0:M])]
for i in range(1,N-M+1):
    c.append(c[-1]-lst[i-1]+lst[i+M-1])
    
print(max(c))
# for i in range(N):
#     c[i] = sum(lst[i:i+M])

# print(max(c))