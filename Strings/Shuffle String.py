s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
dic = {}
res = ""
for i, j in zip(s, indices):
    dic[j] = i
for i in sorted(dic.items()):
    res += i[1]
print(res)