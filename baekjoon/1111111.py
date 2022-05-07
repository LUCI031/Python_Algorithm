def solution(phone_book):
    answer = True
    dic = {}
    for i in phone_book:
        dic[i] = 1

    for i in phone_book:
        temp = ''
        for j in i:
            temp += j

            if temp in dic and temp != i:
                answer =  False

    return answer