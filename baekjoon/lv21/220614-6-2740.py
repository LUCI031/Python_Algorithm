import sys
input=sys.stdin.readline

N,M=map(int,input().split())
MatA=[list(map(int,input().split())) for _ in range(N)]

M,K=map(int,input().split())
MatB=[list(map(int,input().split())) for _ in range(M)]

Mat=[[] for _ in range(N)]
count=0

for n in range(N):
  for k in range(K):
    Num=0
    for m in range(M):
      Num+=MatA[n][m]*MatB[m][k]
    Mat[count].append(Num)
  if count<M:
    count+=1

for i in Mat:
  print(" ".join(list(map(str,i))))