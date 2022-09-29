import sys
input = sys.stdin.readline

N = int(input())
ques = []
for _ in range(N): ques.append(input().strip())

for word in ques:
    flag = False
    left = 0
    right = len(word) - 1
    while left < right:
        # 1. left right 문자 동일한 경우
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            if left < right - 1:
                tmp = word[:right]+word[right+1:]
                if tmp == tmp[::-1]:
                    print(1)
                    flag = True
                    break
            if left + 1 < right:
                tmp = word[:left]+word[left+1:]
                if tmp[:] == tmp[::-1]:
                    print(1)
                    flag = True
                    break
            print(2)
            flag = True
            break
    if not flag:
        print(0)