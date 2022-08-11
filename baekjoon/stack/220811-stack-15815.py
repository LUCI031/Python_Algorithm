import sys
input = sys.stdin.readline

exp = list(input().strip())
arith_checker = ['+', '-', '*', '/']
nums = []

def arith_m(a,b,word):
    if word == '+':
        nums.append(a+b)
    elif word == '-':
        nums.append(a-b)
    elif word == '*':
        nums.append(a*b)
    else:
        nums.append(a//b)

for i in range(len(exp)):
    if exp[i] in arith_checker:
        b = int(nums.pop())
        a = int(nums.pop())
        arith_m(a,b,exp[i])
    else:
        nums.append(exp[i])

if nums:
    print(nums[0])
else:
    print(exp)