import sys
input=sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
org = []

uni_lst = sorted(list(set(lst)))

lst_dict = {i:v for v,i in enumerate(uni_lst)}

for i in lst:
    print(lst_dict[i], end=' ')