import sys
input=sys.stdin.readline

K,N = map(int,input().split())
lst = []

for i in range(K):
    lst.append(int(input()))

left = 1
right = max(lst)
mid = (left + right) // 2

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    
    for n in lst:
        cnt += n // mid
    
    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1
        
print(right)