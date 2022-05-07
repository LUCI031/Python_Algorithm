# 일단 생각나는 대로 
import sys
input=sys.stdin.readline
axis = []

for i in range(3):
    axis.append(list(map(int,input().split())))

p1 = axis[0]
p2 = axis[1]
p3 = axis[2]
p4 = [0,0]


if p1[0] == p2[0]:
    p4[0] = p3[0]
elif p1[0] == p3[0]:
    p4[0] = p2[0]
elif p2[0] == p3[0]:
    p4[0] = p1[0]
    
if p1[1] == p2[1]:
    p4[1] = p3[1]
elif p1[1] == p3[1]:
    p4[1] = p2[1]
elif p2[1] == p3[1]:
    p4[1] = p1[1]
        
print(f"{p4[0]} {p4[1]}")

#모범 답안
# x_nums = []
# y_nums = []
# for _ in range(3):
#     x, y = map(int, input().split())
#     x_nums.append(x)
#     y_nums.append(y)

# for i in range(3):
#     if x_nums.count(x_nums[i]) == 1:
#         x4 = x_nums[i]
#     if y_nums.count(y_nums[i]) == 1:
#         y4 = y_nums[i]
# print(x4, y4)
    