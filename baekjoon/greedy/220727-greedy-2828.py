import sys
input = sys.stdin.readline

N, M = map(int,input().split())

J = int(input())
lst = []

for _ in range(J):
    lst.append(int(input()))
left = 1
right = M
cnt = 0
for num in lst:
    if num <= left:
        cnt += left-num
        right -= left-num
        left -= left-num
        
    elif num >= right:
        cnt += num-right
        left += num-right
        right += num-right
        
print(cnt)