import sys
input = sys.stdin.readline

n,s,r = map(int,input().split())
lst_a = set(map(int,input().split()))
lst_b = set(map(int,input().split()))

lst_a2 = list(lst_a - lst_b)
lst_a3 = list(lst_a - lst_b)
lst_b2 = list(lst_b - lst_a)

for a in lst_a2:
    nx = [-1,1]
    for n in nx:
        if a+n in lst_b2:
            lst_a3.remove(a)
            lst_b2.remove(a+n)
            break

print(len(lst_a3))