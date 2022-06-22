import sys
input=sys.stdin.readline

N,C = map(int,input().split())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort()

left = 1
right = lst[-1]-lst[0]
result = 0

while left <= right:
    mid = (left + right) // 2
    old = lst[0]
    cnt = 1
    
    for i in lst:
        if i - old >= mid:
            cnt += 1
            old = i
    
    if cnt >= C:
        left = mid + 1
        result = mid
    else:
        right = mid - 1
    
print(result)


