import sys
input=sys.stdin.readline

lst = list(input().strip())
answer = []
cnt = 0
for i in range(len(lst)):
    for j in range(i,len(lst)):
        word = ''.join(lst[i:j+1])
        answer.append(word)

print(len(set(answer)))