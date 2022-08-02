import sys
input = sys.stdin.readline

sums = 0
vs = 0
lst = []
lst1 = []
lst2 = []
for _ in range(11):
    d,v = map(int,input().split())
    lst.append([d,v])

lst.sort(key=lambda x:(x[0],x[1]))

for i in range(11):
    lst1.append(lst[i][0])
    lst2.append(lst[i][1])

for i in range(1,len(lst)+1):
    sums += sum(lst1[:i]) + lst2[i-1]*20
print(sums)