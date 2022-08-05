import sys
input = sys.stdin.readline
from collections import Counter as c

words = list(input().strip())

lst = c(words)
lst = sorted(lst.items())
state = ""
word = ""
for alpha in lst:
    a = alpha[0]
    cnt = alpha[1]
    if cnt%2 == 1:
        if state == "":
            state = a
            word += a*(cnt//2)
        else:
            print("I'm Sorry Hansoo")
            exit()
    else:
        word += a*(cnt//2)

print(word+state+word[-1::-1])