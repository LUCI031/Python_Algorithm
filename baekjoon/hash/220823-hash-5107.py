import sys
input = sys.stdin.readline

res = []

while True:
    N = int(input())
    if N == 0:
        for i in range(len(res)):
            print(i+1, res[i])
        exit()
    dics = {}
    names = []
    cnt = 0
    start = 'none'
    for _ in range(N):
        frm, to = map(str,input().strip().split())
        dics[frm] = to
        names.append(frm)
    
    while names:
        name = names.pop()
        start = name
        while True:
            next1 = dics[name]
            if next1 == start:
                cnt += 1
                break
            else:
                name = next1
                names.remove(name)
    res.append(cnt)