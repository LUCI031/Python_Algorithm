import sys
import heapq as h
input = sys.stdin.readline

cases = int(input())

for qq in range(cases):
    qq += 1
    T = int(input())
    NA, NB = map(int,input().split())
    lst = []
    for i in range(NA+NB):
        start, end = map(str,input().strip().split())
        s_hour, s_min = map(str,start.split(':'))
        e_hour, e_min = map(str,end.split(':'))
        start = int(s_hour)*60 + int(s_min)
        end = int(e_hour)*60 + int(e_min)
        if i < NA:
            h.heappush(lst,([start,end,0]))
        else:
            h.heappush(lst,([start,end,1]))
    ab = [0,0]
    trains = [[],[]]

    while lst:
        train = h.heappop(lst)
        d = train[2]
        if trains[d] and trains[d][0] <= train[0]:
            h.heappop(trains[d])
        else:
            ab[d] += 1
        h.heappush(trains[1-d], train[1]+T)
    print(f"Case #{qq}: {ab[0]} {ab[1]}")