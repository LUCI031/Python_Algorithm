import sys
input = sys.stdin.readline

lines = [[] for _ in range(6)]

N, P = map(int,input().split())
cnt = 0

for _ in range(N):
    line, fret = map(int,input().split())
    line -= 1
    if not lines[line]:
        cnt += 1
        lines[line].append(fret)
        lines[line].sort()
    elif lines[line]:
        if fret not in lines[line]:
            lines[line].append(fret)
            cnt += 1
        lines[line].sort()
        while max(lines[line]) > fret:
            lines[line].pop()
            cnt += 1

print(cnt)