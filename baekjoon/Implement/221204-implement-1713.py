import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
frame = []
frame = deque(frame)
candi_lst = []
v = []
reco_cnt = int(input())
votes = list(map(int,input().split()))
candi = defaultdict(list)
# candi에 들어갈 것 [추천수,추가 시기]

for i in range(reco_cnt):
    # 프레임에 있으면 그냥 표 추가하고 다음으로
    if votes[i] in candi_lst:
        candi[votes[i]][0] += 1
        continue
    # 꽉 찼으면 비워내고 진행
    if len(candi_lst) == n: 
        mins = float('inf')
        exile_candi = []
        for c in candi_lst: # 제일 표 수 적은 사람 골라내기
            if candi[c][0] > mins: continue
            elif candi[c][0] < mins:
                mins = candi[c][0]
                exile_candi = [(candi[c][0],candi[c][1],c)]
            elif candi[c][0] == mins:
                exile_candi.append((candi[c][0],candi[c][1],c))
        exile_candi.sort()
        c = exile_candi[0][2]
        candi[c] = [0,0]
        candi_lst.remove(c)
    # 전에 안나왔던 경우 -> 딕셔너리 선언
    if votes[i] not in v:
        candi[votes[i]] = [1,i]
        v.append(votes[i])
    else: #전에 나왔던 경우 -> 카운트 및 선언 지점 업데이트
        candi[votes[i]][0] += 1
        candi[votes[i]][1] = i
    # 프레임에 다시 추가
    candi_lst.append(votes[i])

candi_lst.sort()
print(*candi_lst)