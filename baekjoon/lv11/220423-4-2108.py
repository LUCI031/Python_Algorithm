from collections import Counter
import sys
input=sys.stdin.readline

nums = []
N = int(input())
for i in range(N):
    nums.append(int(input()))
    
nums.sort()
cnt = Counter(nums).most_common(2)
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        if cnt[1][0] > cnt[0][0]:
            maxi = cnt[1][0]
        else:
            maxi = cnt[0][0]
    else:
        maxi = cnt[0][0]
else:
    maxi = nums[0]  
    
print((round(sum(nums)/len(nums))))
print(nums[len(nums)//2])
print(maxi)
print(max(nums)-min(nums))