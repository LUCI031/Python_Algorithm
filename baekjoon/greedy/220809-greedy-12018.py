import sys
input = sys.stdin.readline

N,M = map(int,input().split())
order = []
lst = []
cnt = 0
for i in range(N):
    p,l = map(int,input().split())
    peep = list(map(int,input().split()))
    peep.sort()
    if M > 0:
        if p-l < 0 :
            M -= 1
            cnt += 1
        else:
            order.append(peep[p-l])

if M > 0:
    order.sort()

    for ord1 in order:
        if M - ord1 >= 0:
            cnt += 1
            M -= ord1
        else:
            break

print(cnt)