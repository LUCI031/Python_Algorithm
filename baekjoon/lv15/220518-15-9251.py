import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000)

str_a = list(input().strip())
str_b = list(input().strip())
LCS = [[0 for i in range(len(str_b)+1)] for i in range(len(str_a)+1)]

for i in range(1,len(str_a)+1):
    for j in range(1,len(str_b)+1):
        if str_a[i-1] == str_b[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
            
print(LCS[-1][-1])