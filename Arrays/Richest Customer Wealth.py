accounts = [[1,2,3],[3,2,1]]

t=[]
for i in range(0,len(accounts)):
    x=0
    print(x)
    for j in accounts[i]:
        x=x+j
        print(j)
    t.append(x)
print(max(t))