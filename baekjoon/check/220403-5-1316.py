# 백준 1316 그룹 체커
import sys
input=sys.stdin.readline

N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0,len(word)-1):
        if word[j] != word[j+1]:
            if word[j] in word[j+1:]:
                cnt -= 1
                break
print(cnt)

# cd /usr/local/mysql/bin
# mysql -uroot -p -P4444

# python3 -m pip install tensorflow-macos