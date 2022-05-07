# 백준 10809 
# 내가 짠  코드
# import sys
# input=sys.stdin.readline

# word = list(str.lower(input()))
# word.remove('\n')
# trans_num = []
# for i in range(0, len(word)):
#     trans_num.append(ord(word[i]))

# for i in range(0, 26):
#     i2 = i + 97
#     if i2 not in trans_num:
#         print(-1,end=' ')
#     elif i2 in trans_num:
#         print(word.index(chr(i2)), end=' ')

# 모범 답안
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x)),end=' ')