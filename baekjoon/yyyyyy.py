for i in range((208//15)+1,0,-1):
    for j in range(0,208//7+1):
        if 7*i + 15j == 208:
            print(i,j)
            break