import sys
input = sys.stdin.readline

while True:
    try:
        s,t = map(str,input().split())
        cnt = 0
        for string in t:
            if string == s[cnt]:
                cnt += 1
            if cnt == len(s):
                print("Yes")
                break
        if cnt < len(s):
            print("No")
    except:
        exit()