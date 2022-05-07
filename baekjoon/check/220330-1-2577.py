# 백준 2577
#내가 푼 답
# a = int(input())
# b = int(input())
# c = int(input())
# output = a*b*c
# cnt = list(map(int, str(output)))
# for i in range(0,10):
#     print(cnt.count(i))

A=int(input()) 
B=int(input()) 
C=int(input()) 

result = list(str(A*B*C)) 

for i in range(10): 
    print(result.count(str(i)))
