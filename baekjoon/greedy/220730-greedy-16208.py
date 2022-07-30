import sys
from collections import deque
input = sys.stdin.readline
result = 0
N = int(input())

lst = list(map(int,input().split()))
lst.sort()
que = deque(lst)
sums = sum(lst)

while que:
    if len(que) != 1:
        mins = que.popleft()
        maxi = que.pop()
        sums -= mins+maxi
        result += mins*maxi
        result += sums * (maxi+mins)
    else:
        que.pop()

print(result)