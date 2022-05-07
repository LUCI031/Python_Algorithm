import sys
input=sys.stdin.readline

N = int(input())
num_list = [0] * 10001

for i in range(N):
    new = int(input())
    num_list[new] += 1

for j in range(len(num_list)):
    if num_list[j] != 0:
        for g in range(num_list[j]):
            print(j)