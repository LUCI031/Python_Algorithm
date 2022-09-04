import sys
input = sys.stdin.readline

res = []
words = input().strip()
state = True
exp = ""

for i in range(len(words)):
    if state == True:
        if words[i] == '<':
            if exp:
                res.append(exp[::-1])
                exp = ""
            state = False
            exp += words[i]
        else:
            if words[i] == ' ':
                res.append(exp[::-1]+' ')
                exp = ""
            else:
                exp += words[i]
    else:
        if words[i] == '>':
            state = True
            res.append(exp+words[i])
            exp = ""
        else:
            exp += words[i]

if exp:
    res.append(exp[::-1])

for word in res:
    print(word,end='')