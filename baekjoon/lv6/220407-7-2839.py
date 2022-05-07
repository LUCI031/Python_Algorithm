import sys
input=sys.stdin.readline

N = int(input())
cnt = 0

if N%5 == 0:
    print(N//5)

else:
    while True:
        N -= 3
        cnt += 1
        
        if N%5 == 0:
            print(cnt+N//5)
            break
        
        elif N==1 or N==2:
            print(-1)
            break
        
        elif N == 0:
            print(cnt)
            break
        
        