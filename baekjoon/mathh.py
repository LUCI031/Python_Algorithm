import math, numpy

vr, vs, wr, ws = map(int,input().split())

v_cos = vr * math.cos(math.pi*(vs/180))
w_cos = wr * math.cos(math.pi*(ws/180))
v_sin = vr * math.sin(math.pi*(vs/180))
w_sin = wr * math.sin(math.pi*(ws/180))
x_ans = v_cos + w_cos
y_ans = v_sin + w_sin

arctan = numpy.arctan(y_ans/x_ans)*180/math.pi

length = math.sqrt(y_ans**2+x_ans**2)

if x_ans > 0 and y_ans > 0:
    print(x_ans,y_ans,arctan,length)
elif x_ans < 0 and y_ans > 0:
    print(x_ans,y_ans,180+arctan,length)
elif x_ans < 0 and y_ans < 0:
    print(x_ans,y_ans,180+arctan,length)
else:
    print(x_ans,y_ans,360+arctan,length)