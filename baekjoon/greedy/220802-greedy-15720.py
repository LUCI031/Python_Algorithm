import sys
input = sys.stdin.readline

b,c,d = map(int,input().split())
lst = []
org = 0
sale = 0
rest = 0

for _ in range(3):
    nums = list(map(int,input().split()))
    nums.sort()
    org += sum(nums)
    lst.append(nums)


for _ in range(min(b,c,d)):
    for prices in lst:
        sale += prices.pop()

for prices in lst:
    rest += sum(prices)

print(org)
print(rest+int(sale*0.9))