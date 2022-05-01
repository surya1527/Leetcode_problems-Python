image = [[1,1,0],[1,0,1],[0,0,0]]
res = []
for i in image:
    i.reverse()
    lis = []
    for j in i:
        if j == 0:
            lis.append(1)
        else:
            lis.append(0)

    res.append(lis)

print(res)
