import sys
input=sys.stdin.readline

N = int(input())

case = list(map(int, input().split()))
rev_case = case[::-1]

a_ups = [1 for i in range(N)]
downs = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if case[i] > case[j]:
            a_ups[i] = max(a_ups[i], a_ups[j]+1)
        if rev_case[i] > rev_case[j]:
            downs[i] = max(downs[i],downs[j]+1)

result = [0 for i in range(N)]           
for k in range(N):
    result[k] = a_ups[k] + downs[N-k-1]-1
    
print(max(result))
        
# dp_up = [1] * N
# dp_down = [1] * N
# ans = []
# for i in range(N):
#     for j in range(i):
#         if A[j]<A[i]:
#             dp_up[i] = max(dp_up[i],dp_up[j]+1)
#         elif A[j]>A[i]:
#             dp_down[i] = max(dp_down[i],dp_down[j]+1)

# for j in range(N):
#     ans.append(dp_up[j]+dp_down[N-j-1]-1)

# print(print(max(ans)))