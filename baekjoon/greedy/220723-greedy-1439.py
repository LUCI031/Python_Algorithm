import sys
input = sys.stdin.readline

S = input().strip()
letter = S[0]
state = True
cnt1 = 1
cnt2 = 0

for i in range(1,len(S)):
    if S[i] != letter:
        if state:
            cnt2 += 1
            state = False
            letter = S[i]
        else:
            cnt1 += 1
            state = True
            letter = S[i]

print(min(cnt1,cnt2))