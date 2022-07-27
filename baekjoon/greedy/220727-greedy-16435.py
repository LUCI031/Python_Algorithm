import sys
input = sys.stdin.readline

N,L = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort(reverse=True)
while lst:
    feed = lst.pop()
    if L >= feed:
        L += 1
    else:
        break
print(L)