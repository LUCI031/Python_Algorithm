import sys
input=sys.stdin.readline

def partner(a):
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            print(f"{a[i]} - {a[j]}")
    
names = ["Tom", "Jerry", "Mike"]
partner(names)
name2 = ["Tom", "Jerry", "Mike", "John"]
partner(name2)