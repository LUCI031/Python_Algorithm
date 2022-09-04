def solution(rule, A, B):
    base = len(rule) # N진법 표기
    a = [0] * len(A) # a = [0 for _ in range(len(A))]
    b = [0] * len(B)
    str2int, int2str = dict(), dict()
    idx_a, pos = 0, 0
    answer = ''

    for idx, char in enumerate(rule): # 변환표
        str2int[char] = idx
        int2str[idx] = char

    for i in range(len(A)): # 문자를 진법 수로 변환(list)
        a[i] = str2int[A[i]]
    for j in range(len(B)):
        b[j] = str2int[B[j]]

    if a == b: # 예외 처리
        return rule[0] # 0에 해당하는 문자 출력

    while b: # a를 pop할 경우 a에서 받아내림 case를 처리할 수 없음 (진법 가릿수 계산) ★★
        b_num = b.pop() # 가감의 절차는 뒤에서부터 함
        idx_a = (len(A)-1) - pos

        if b_num == 0: # 예외 처리
            pos += 1
            continue
        if a[idx_a] <= 0: # Case 1. 연산하는 a의 값이 0일 경우 or Case 2. 연산하는 a의 값이 음수인 경우(뒷자리에서 받아내림해주었을 때 발생함)
            a[idx_a] += base
            a[idx_a -1] -= 1
            a[idx_a] -= b_num
        elif a[idx_a] - b_num >= 0: # Case 3. 일반적인 경우
            a[idx_a] -= b_num
        else: # Case 4. 자릿수의 차가 음수인 경우
            a[idx_a] += base
            a[idx_a -1] -=1
            a[idx_a] -= b_num
        pos += 1


    for idx in range(len(a)): # 계산한 결과를 변환표를 통해 문자열로 변환
        if not answer and a[idx] == 0: # 예외 처리(★): ex) 005은 3으로 표현 + 105 같은 경우는 제외(not answer)
            continue
        else:
            answer += int2str[a[idx]]

    return answer

print(solution('abcde','bcdd','ddd'))
