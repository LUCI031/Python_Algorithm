import sys
input=sys.stdin.readline

N = int(input())
ans = 0
lst = list(map(int, input().split()))
lst.sort()

for i in range(N):
    ans += sum(lst[:i+1])
    
print(ans)