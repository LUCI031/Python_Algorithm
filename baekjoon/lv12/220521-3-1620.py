import sys
input=sys.stdin.readline

N,M = map(int,input().split())
dict = {} 
lst = []

for i in range(1,N+1):
    dict[input().strip()] = i
    
for i in range(M):
    a = input().strip()
    lst.append(a)
a = list(dict.items())
for i in range(M):
    if 47 < ord(lst[i][0]) < 58:
        print(a[int(lst[i])-1][0])
    else:
        print(dict[lst[i]])