import sys
input=sys.stdin.readline

N = int(input())

km = list(map(int,input().split()))
st = list(map(int,input().split()))
st = st[:-1]
price = st[0]
dist = km[0]
result = 0

for i in range(N-2):
    if st[i+1] >= price:
        dist += km[i+1]
    else:
        result += price * dist
        dist = km[i+1]
        price = st[i+1]

result += price*dist
print(result)