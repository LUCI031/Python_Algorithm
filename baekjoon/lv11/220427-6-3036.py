import sys
input=sys.stdin.readline

N = int(input())
wheels = list(map(int,input().split()))
x_lst = []
y_lst = []

for i in range(1,len(wheels)):
    cnt = 1
    if wheels[0]%wheels[i] == 0:
        x_lst.append(int(wheels[0])//wheels[i])
        y_lst.append(1)
    else:
        while (cnt*wheels[0])%wheels[i] != 0:
            cnt += 1
        x_lst.append(int(cnt*wheels[0])//wheels[i])
        y_lst.append(cnt)
        
for x,y in zip(x_lst,y_lst):
    print(f'{x}/{y}')