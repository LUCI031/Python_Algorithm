import sys
input=sys.stdin.readline

def fivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fivo(n-1) + fivo(n-2)
    
N = int(input())
print(fivo(N))

# 모범답안
# def fibo(n):
#     return fibo(n - 1) + fibo(n - 2) if n > 1 else n


# print(fibo(int(input())))