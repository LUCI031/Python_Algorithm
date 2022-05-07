# 방향 가짓수 x->0 / y->0 / w -> 0 / h -> 0
# 일단 푸는데 성공하고 고민 시작

import sys
input=sys.stdin.readline

x,y,w,h = map(int,input().split())

# 내가 푼 공식
# vertical = 0
# horizon = 0
# steps = 0

# if w-x <= x:
#     vertical = w-x
# else:
#     vertical = x
# if h-y <= y:
#     horizon = h-y
# else:
#     horizon = y

# if vertical >= horizon:
#     steps = horizon
# else:
#     steps = vertical
    
# print(steps)

# 모범 답안
print(min(x,y,w-x,h-y))