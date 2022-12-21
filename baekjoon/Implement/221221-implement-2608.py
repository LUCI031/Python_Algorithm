import sys
from collections import deque
input = sys.stdin.readline

dics1 = {'I':1,'X':10,'C':100,'M':1000,'V':5,'L':50,'D':500}
dics2 = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

def alpha_to_num(a):
    result = 0
    a_lst = list(a)
    for words in list(dics2.keys()):
        pos = a.find(words)
        if  pos != -1:
            result += dics2[words]
            a_lst[pos] = 'S'
            a_lst[pos+1] = 'S'

    a = ''.join(a_lst)
    for words in list(dics1.keys()):
        cnt = a.count(words)
        result += dics1[words] * cnt
    return result

def num_to_alpha(s_num):
    num = list(map(int,str(s_num)))
    answer = ''
    lst = []
    # 일의 자리 
    a = int(num[-1])
    if a < 4:
        answer += 'I' * num[-1]
    elif a == 4:
        answer += 'IV'
    elif a == 5:
        answer += 'V'
    elif 5 < a < 9:
        answer += 'V'
        answer += 'I'*(a-5)
    else:
        answer += 'IX'
    lst.append(answer)
    answer = ''
    #십의 자리
    if len(num) > 1:
        a = int(num[-2])
        if a < 4:
            answer += 'X' * a
        elif a == 4:
            answer += 'XL'
        elif a == 5:
            answer += 'L'
        elif 5 < a < 9:
            answer += 'L'
            answer += 'X'*(a-5)
        else:
            answer += 'XC'
        lst.append(answer)
        answer = ''

    # 백의 자리
    if len(num) > 2:
        a = int(num[-3])
        if a < 4:
            answer += 'C' * a
        elif a == 4:
            answer += 'CD'
        elif a == 5:
            answer += 'D'
        elif 5 < a < 9:
            answer += 'D'
            answer += 'C'*(a-5)
        else:
            answer += 'CM'
        lst.append(answer)
        answer = ''

    # 천의 자리
    if len(num) > 3:
        a = int(num[0])
        answer += 'M' * a
        lst.append(answer)
        answer = ''
    
    lst.reverse()
    answer = ''.join(lst)
    return answer

a = input().strip()
b = input().strip()

print(alpha_to_num(a)+alpha_to_num(b))
print(num_to_alpha(alpha_to_num(a)+alpha_to_num(b)))