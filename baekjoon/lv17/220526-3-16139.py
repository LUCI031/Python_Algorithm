import sys
input=sys.stdin.readline

S = input()
q = int(input())

for i in range(q):
    ques = list(input().split())
    sys.stdout.write(str(S[int(ques[1]):int(ques[2])+1].count(ques[0]))+'\n')
    
# 100점
# import sys
# #sys.stdin=open('input.txt')

# s = sys.stdin.readline()
# n = int(sys.stdin.readline())

# lis=[]

# # @profile
# def prep():
#     for c in 'abcdefghijklmnopqrstuvwxyz':
#         cnt=0
#         tmp=[]
#         for item in str(s):
#             if item==c:
#                 cnt+=1
#             tmp.append(cnt)
#         lis.append(tmp)

# # @profile
# def main():
#     global n
#     while n:
#         n-=1
#         tmp = sys.stdin.readline().split()
#         c, start, end = tmp[0], int(tmp[1]), int(tmp[2])
#         tmp_lis = lis[ord(tmp[0])-97]
#         answer=tmp_lis[end]-tmp_lis[start]
#         if s[start]==c:
#             answer+=1
#         sys.stdout.write(str(answer)+'\n')
#         # print(answer)
# if __name__ == "__main__":
#     prep()
#     main()
# 출처: https://joey09.tistory.com/134 [joie de vivre:티스토리]