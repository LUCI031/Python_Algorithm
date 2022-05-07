import sys
input=sys.stdin.readline

N = int(input())
cnt = 0
num = 666
while N != cnt:
    if '666' in str(num):
        cnt += 1
    num += 1
    
print(num-1)