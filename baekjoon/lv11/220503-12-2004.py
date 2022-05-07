# import sys, math
# input=sys.stdin.readline

# n,m = map(int,input().split())
# cnt = 0
# def facto(a):
#     if a == 0:
#         return 1
#     else:
#         return a * facto(a-1)
    
# number = str(facto(n)//(facto(m)*facto(n-m)))

# for i in range(len(number)-1,-1,-1):
#     if number[i] == '0':
#         cnt += 1
#     else:
#         break
# print(N//5 + N//25 + N//125)
# print(cnt)

import sys
input=sys.stdin.readline
n, m = map(int, input().split())

def cnt2(n):
    n2 = 0
    while(n != 0):
        n //= 2
        n2 += n
    return n2

def cnt5(n):
    n5 = 0
    while(n != 0):
        n //= 5
        n5 += n
    return n5

print(min(cnt2(n)-cnt2(m)-cnt2(n-m), cnt5(n)-cnt5(m)-cnt5(n-m)))

   1 2 3 4 5 6 7 8 9 10         23 24 25 
5          1          1                1  