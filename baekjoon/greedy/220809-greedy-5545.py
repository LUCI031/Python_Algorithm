import sys
input = sys.stdin.readline

N = int(input())
A,B = map(int,input().split())
C = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
sums = C
cnts = A
price = sums/cnts

for i in range(N):
    price = sums/cnts
    if (sums+lst[i])/(cnts+B) > price:
        sums += lst[i]
        cnts += B
    else:
        print(int(price))
        exit()
        
price = sums/cnts
print(int(price))