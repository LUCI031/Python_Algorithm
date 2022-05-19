import sys
input=sys.stdin.readline

while True:
    trianlge = list(map(int,input().split()))
    if trianlge.count(0) == 3:
        break
    else:
        hypo = max(trianlge)
        others = 0
        trianlge.remove(hypo)

        for i in trianlge:
            others = others + i**2
            
        if others == hypo**2:
            print('right')
        else:
            print('wrong')