import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()
lst = []
lst.append(T)
while lst:
    word = lst.pop()
    if word == S:
        print(1)
        exit()
    # case 1: add A
    if len(word) < len(S):
        continue
    if word[-1] == 'A':
        lst.append(word[:-1])
    # case 2: reverse and B
    if word[0] == 'B':
        r_word = word[1:]
        lst.append(r_word[::-1])
print(0)