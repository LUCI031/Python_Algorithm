import sys
input=sys.stdin.readline


X = int(input())
steps = 1
#위치 찾기
while True:
    if X > steps:
        X -= steps
        steps += 1
    else:
        break

if steps%2 == 0:
    top = X
    under = steps-X+1
else:
    top = steps-X+1
    under = X
    
print(f"{top}/{under}")

# X = int(input())
# stage, key_X = 1, 1
# while key_X + stage <= X:
#     key_X += stage
#     stage += 1
# step = X - key_X
# x, y = step + 1, stage - step
# if stage % 2 == 0:
#     print('{}/{}'.format(x, y))
# else:
#     print('{}/{}'.format(y, x))
 
# 1칸 2칸 3칸 4칸 차이
# 홀 짝 차이 있음 홀일 땐 감소 짝일 땐 증가