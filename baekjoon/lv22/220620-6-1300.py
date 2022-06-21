import sys
input=sys.stdin.readline

N = int(input())
K = int(input())
result = 0
start = 1
end = K

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in range(1,N+1):
        tmp += min(mid//i,N)
    
    if tmp < K:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)


# 1 2 3
# 2 4 6
# 3 6 9