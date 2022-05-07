# 백준 1065 한수
# 8줄에 cnt == N 했다가 한참 틀림
import sys
input=sys.stdin.readline
def hansu(N):
    cnt = 0
    if N < 100:
        cnt = N
        return cnt
    else:
        cnt = 99
        for i in range(100, N+1):
            nums = list(map(int, str(i)))
            if nums[0] - nums[1] == nums[1] - nums[2]:
                cnt += 1
    return cnt
ques = int(input())
print(hansu(ques))