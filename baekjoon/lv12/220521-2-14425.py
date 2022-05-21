import sys
input=sys.stdin.readline

N, M = map(int, input().split())

dict = {}
lst = []
cnt = 0

for _ in range(N):
    a = input().strip()
    dict[a] = 0
    
for _ in range(M):
    lst.append(input().strip())
    
for i in range(M):
    if lst[i] in dict:
        cnt += 1

print(cnt)