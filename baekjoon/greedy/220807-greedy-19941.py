import sys
input = sys.stdin.readline

N,K = map(int,input().split())
words = list(input())
cnt = 0
nx = []
check = False
if N == 1:
    print(0)
    exit()

for i in range(1,K+1):
    nx.append(i)
    nx.append(-i)
nx.sort()

for i in range(N):
    if words[i] == 'P':
        check = False
        for x in nx:
            idx = x + i
            if idx < 0 or idx > N :
                continue
            if words[idx] == 'H' and check == False:
                words[idx] = 'x'
                words[i] = 'x'
                cnt += 1
                check = True

print(cnt)