import sys
import re
input = sys.stdin.readline

def dfs (word,i):
    arith = [' ','+', '-']
    if i != N-1:
        for k in range(3):
            dfs(word+arith[k]+str(i+1),i+1)
    else:
        for k in range(3):
            aaa.append(word+arith[k]+str(i+1))
        
T = int(input())

for _ in range(T):
    aaa = []
    N = int(input())
    dfs(str(1),1)
    for word in aaa:
        if eval(word.replace(" ","")) == 0:
            print(word)
    print()