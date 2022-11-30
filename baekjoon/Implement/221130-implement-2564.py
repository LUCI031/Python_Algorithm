import sys
input = sys.stdin.readline

def get_dis(x,y):
    if x == 1:
        return y
    elif x == 2:
        return w+h+w-y
    elif x == 3:
        return 2*(w+h)-y
    else:
        return w+y

w,h = map(int,input().split())

n = int(input())
course = []
for _ in range(n+1):
    x,y = map(int,input().split())
    course.append(get_dis(x,y))

ans = 0
for i in range(n):
    ins = abs(course[-1]-course[i])
    outs = 2*(w+h)-ins
    ans += min(ins,outs)

print(ans)
