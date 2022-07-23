import sys
input = sys.stdin.readline

lst = []
cnt = 1

while True:
    a,b,c = map(int,input().split())
    if a == b == c == 0:
        break
    lst.append((a,b,c))

if len(lst) > 1:
    for case in lst:
        ans = 0
        L = case[0]
        P = case[1]
        V = case[2]
        ans += (V//P) * L
        rest = V%P
        if rest < L:
            ans += rest
        else:
            ans += L
        print(f"Case {cnt}: {ans}")
        cnt += 1