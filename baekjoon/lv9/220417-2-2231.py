# 예전에 비슷한 유형 풀었던 것 생각나서 찾아봄
# 한수에서 비슷한 개념 썼던 것 같아서 활용

import sys
input=sys.stdin.readline

N = int(input())

for i in range(N+1):
    nums = list(map(int, str(i)))
    if sum(nums) + i == N:
        print(i)
        break
    elif i == N:
        print(0)