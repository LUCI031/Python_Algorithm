import sys
input=sys.stdin.readline

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))
    
nums = sorted(nums)
for i in nums:
    print(i)
