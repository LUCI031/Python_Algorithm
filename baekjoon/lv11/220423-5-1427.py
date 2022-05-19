import sys
input=sys.stdin.readline

N = list(str(input()))
N.remove('\n')
N.sort(reverse=True)
print(*N,sep='')
