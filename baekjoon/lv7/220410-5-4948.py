import sys
input=sys.stdin.readline

def isPrime(N):
    nums = [True] * (N+1)
    m = int(N**0.5)+1
    if N==1:
        pass
    else:
        for i in range(2, m):
            if nums[i] == True:
                for j in range(2*i,N+1,i):
                    nums[j] = False
    return [i for i in range(2, N+1) if nums[i] == True]

n = 1
while n > 0:
    n = int(input())
    if n == 1:
        print(1)
    elif n == 0:
        break
    else:
        num_n = set(isPrime(n))
        num_2n = set(isPrime(2*n))
        print(len(num_2n-num_n))
    