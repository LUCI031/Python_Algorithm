import sys
input=sys.stdin.readline

N,K = map(int,input().split())
lst = []
cnt = 0
for i in range(N):
    lst.append(int(input()))

lst.sort(reverse=True)

while K != 0:
    for i in range(N):
        if K/lst[i] >= 1:
            cnt += K//lst[i]
            K = K - K//lst[i]*lst[i]
            
print(cnt)