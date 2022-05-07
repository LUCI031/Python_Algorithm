import sys # , itertools
input=sys.stdin.readline

def facto(a):
    if a == 0:
        return 1
    return a*facto(a-1)

N = int(input())

for i in range(N):
    n, m = map(int,input().split())
    print(facto(m)//(facto(m-n)*facto(n)))

# for i in range(N):
#     n, m = map(int,input().split())
#     b = [i for i in range(m)]
#     ans = len(list(itertools.combinations(b,n)))
#     print(ans)

