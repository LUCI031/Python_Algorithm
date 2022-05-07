import sys
input=sys.stdin.readline

while True:
    x,y = map(int,input().split())
    if x == 0 and y == 0:
        break
    elif x<y and (y/x)%1 == 0:
        print('factor')
    elif x>y and (x/y)%1 == 0:
        print('multiple')
    else:
        print('neither')