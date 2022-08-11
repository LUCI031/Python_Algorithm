import sys
input = sys.stdin.readline
from collections import defaultdict, deque

N = int(input())
exp = list(input().strip())
dics = defaultdict(int)
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
        nums.append(a/b)

for i in range(N):
    dics[chr(i+65)] = int(input())

for i in range(len(exp)):
    if exp[i] in arith_checker:
        b = nums.pop()
        a = nums.pop()
        arith_m(a,b,exp[i])
    else:
        nums.append(dics[exp[i]])

print("{:.2f}".format(nums[0]))