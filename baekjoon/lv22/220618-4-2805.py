import sys
input=sys.stdin.readline

K,N = map(int,input().split())

lst = list(map(int,input().split()))

left = 1
right = max(lst)
mid = (left + right) // 2

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    
    for i in lst:
        if i > mid:
            cnt += i-mid 
    
    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1
        
print(right)