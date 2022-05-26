# https://jae04099.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1463-1%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0
import sys
input=sys.stdin.readline

N = int(input())
d = [0]*(N+1)

for i in range(2, N+1):
    d[i] = d[i-1]+1
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2]+1)
print(d[N])