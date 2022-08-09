import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))

sums = 0
lst.sort(reverse=True)
for num in lst:
    if sums < num:
        sums = (sums/2) + num
    else:
        sums += (num/2)

print(sums)