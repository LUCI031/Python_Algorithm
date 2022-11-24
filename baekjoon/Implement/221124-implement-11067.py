# from collections import defaultdict
import sys
input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#     dics = defaultdict(list)
#     x_lst = []
#     last_y = 0
#     result = [[0,0]]

#     n = int(input())
#     for _ in range(n):
#         x,y = map(int,input().split())
#         dics[x].append(y)
#         x_lst.append(x)
#     x_lst = set(x_lst)
#     x_lst = list(x_lst)
#     x_lst.sort(reverse=True)
#     ques = (list(map(int,input().split())))

#     while x_lst:
#         cur_x = x_lst.pop()
#         cur_lst = dics[cur_x]
#         max1 = max(cur_lst)
#         if max1 == last_y:
#             cur_lst.sort(reverse=True)
#         else:
#             cur_lst.sort

#         for yy in cur_lst:
#             if cur_x == 0 and yy == 0:
#                 continue
#             else:
#                 result.append([cur_x,yy])
#         last_y = result[-1][1]
            
#     for ques_pos in ques[1:]:
#         ques_pos -= 1
#         print(*result[ques_pos])

import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):   
    n = int(input())    
    answer = [[0, 0]]
    dic = {}
    
    for j in range(n):
        x, y = map(int, input().split())
        if x not in dic:
            dic[x] = list()
        dic[x].append(y)
        
    sdic = sorted(dic.items())

    for j in range(len(sdic)):
        sdic[j][1].sort()
        if answer[-1][1] != sdic[j][1][0]:
            sdic[j][1].sort(reverse = True)   
        for k in range(len(sdic[j][1])):
            answer.append([sdic[j][0], sdic[j][1][k]])
            
    m = list(map(int, input().split()))

    for j in range(1, len(m)):
        print(*(answer[m[j]]))