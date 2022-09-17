import sys
from collections import deque
input = sys.stdin.readline

def check_right (start,d):
    if start > 4 or gears[start-1][2] == gears[start][6]:
        return
    
    if gears[start-1][2] != gears[start][6]:
        check_right(start+1,-d)
        gears[start].rotate(d)

def check_left (start,d):
    if start < 1 or gears[start][2] == gears[start+1][6]:
        return
    
    if gears[start][2] != gears[start+1][6]:
        check_left(start-1,-d)
        gears[start].rotate(d)

gears = {}

for i in range(1,5):
    gears[i] = deque(list(map(int, list(input().strip()))))
n = int(input())

for _ in range(n):
    num, dirs = map(int,input().split()) 

    check_right(num+1,-dirs)
    check_left(num-1,-dirs)
    gears[num].rotate(dirs)

result = 0
for i in range(4):
    result += (2**i) * gears[i+1][0]

print(result)