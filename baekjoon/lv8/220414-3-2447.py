# 재귀로 하는 건 알겠지만 구현을 모르겠음
# 큰 반복 안에 작은 반복 넣는 것 같음
# 프렉탈 도형 그리는 문제, 분할 
# https://imgzon.tistory.com/37 이게 제일 잘함

# import sys
# input=sys.stdin.readline

# def star(a):
#     if a == 3:
#         return ['***','* *','***']
    
#     arr = star(a//3)
#     stars = []
    
#     for i in arr:
#         stars.append(i*3)
        
#     for i in arr:
#         stars.append(i+' '*(a//3)+i)
        
#     for i in arr:
#         stars.append(i*3)
        
#     return stars
# n = int(input())
# print('\n'.join(star(n)))

import sys
sys.setrecursionlimit(10**6)

def paint_star(LEN):
  DIV3 = LEN//3

  if LEN == 3:
    g[1] = ['*', ' ', '*'] 
    g[0][:3] = g[2][:3] = ['*']*3 
    return 
  
  paint_star(DIV3) 
  
  for i in range(0, LEN, DIV3): 
    for j in range(0, LEN, DIV3): 
      if i != DIV3 or j != DIV3: 
        for k in range(DIV3): 
          g[i+k][j:j+DIV3] = g[k][:DIV3] 


n = int(input())
g = [[' ' for _ in range(n)] for _ in range(n)] 

paint_star(n)

for i in range(n): 
  for j in range(n): 
    print(g[i][j], end='') 

  print()