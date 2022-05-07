import sys
input=sys.stdin.readline

N = int(input())
lst = [0]*101
lst[0] = 1
lst[1] = 1
lst[2] = 1
lst[3] = 1

def nums(a):
    if a-1 < 3 or lst[a] != 0:
        return lst[a]
    else:
        lst[a] = nums(a-2) + nums(a-3)
        return lst[a]

for i in range(N):
    a = int(input())
    print(nums(a))