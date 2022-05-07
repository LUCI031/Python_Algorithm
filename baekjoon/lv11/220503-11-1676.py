

# import sys
# input=sys.stdin.readline

# def facto(a):
#     if a == 0:
#         return 1
#     else:
#         return a * facto(a-1)

# N = int(input())
# number = str(facto(N))
# cnt = 0
# for i in range(len(number)-1,-1,-1):
#     if number[i] == '0':
#         cnt += 1
#     else:
#         break
# print(cnt)
# https://lucian-blog.tistory.com/84?category=1034989
N = int(input())
print(N//5 + N//25 + N//125)