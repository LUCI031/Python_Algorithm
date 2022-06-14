import sys
input=sys.stdin.readline

N,K = map(int,input().split())
p = 1000000007

def facto(a):
    q = 1
    for i in range(2,a+1):
        q = (q*i) % p
    return q

def square(b,c):
    if c == 0:
        return 1
    elif c == 1:
        return b
    
    tmp = square(b,c//2)
    if c % 2:
        return tmp * tmp * b % p
    else:
        return tmp * tmp % p
    
top = facto(N)
bot = facto(N-K) * facto(K) % p

print(top * square(bot, p-2) % p)