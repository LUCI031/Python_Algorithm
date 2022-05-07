# def solution(genres, plays):
#     hits = {}
#     for i in range(len(genres)):
#         if genres[i] not in hits.keys():
#             hits.update({genres[i]:plays[i]})
#         else:
#             hits[genres[i]].update(plays[i])
#     return hits
# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays= [500, 600, 150, 800, 2500]

# print(solution(genres, plays))

def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
genres = ["classic", "pop", "classic", "classic", "pop"]
plays= [500, 600, 150, 800, 2500]

print(solution(genres, plays))

# 딕셔너리 만들고 밸류 추가
