import sys

def divdeandconquer(a):
    if len(a) == 1:
        return a[0]
    if len(a) % 2 == 1:
        a = [0] + a
    d = len(a) // 2
    x = a[:d]
    y = a[d:]
    cnt = 2
    tmpmax = min(a[d - 1], a[d])
    tmparea = tmpmax * cnt
    i = 0
    j = 0
    for _ in range(0, len(a) - 2):
        if d - 1 - i == 0:
            j += 1
        elif d + j == len(a) - 1:
            i += 1
        else:
            if a[d - 2 - i] >= a[d + 1 + j]:
                i += 1
            else:
                j += 1
        tmpmax = min(tmpmax, a[d - 1 - i], a[d + j])
        cnt += 1
        tmparea = max(tmparea, tmpmax * cnt)
    z = tmparea
    return max(divdeandconquer(x), divdeandconquer(y), z)


while 1:
    n, *histogram = list(map(int, sys.stdin.readline().split()))
    if n == 0:
        break
    maxarea = divdeandconquer(histogram)
    print(maxarea)