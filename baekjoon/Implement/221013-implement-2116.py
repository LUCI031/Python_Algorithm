import sys
input = sys.stdin.readline

N = int(input())
lst = []
result = [0]*N
for _ in range(N):
    lst.append(list(map(int,input().split())))
rotate = {0:5,1:3,2:4,3:1,4:2,5:0}

for i in range(6):
    max_lst = []
    dice = [1+i for i in range(6)]
    bottom = lst[0][i]
    top = lst[0][rotate[i]]
    dice.remove(bottom)
    dice.remove(top)
    max_lst.append(max(dice))
    for j in range(1,N):
        dice = [1+i for i in range(6)]
        bottom = top
        dice.remove(bottom)
        top = lst[j][rotate[lst[j].index(top)]]
        dice.remove(top)
        max_lst.append(max(dice))
    result.append(sum(max_lst))

print(max(result))