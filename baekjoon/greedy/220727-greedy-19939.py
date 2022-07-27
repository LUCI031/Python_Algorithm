import sys
input = sys.stdin.readline

N,K = map(int,input().split())
sums = K*(K+1)//2
if N < sums:
    print(-1)
else:
    if (N-sums)%K == 0:
        print(K-1)
    else:
        print(K)
