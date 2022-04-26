paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
d={}
for i in paths:
    d[i[0]]=i[1]
print(d)
print(d.values())
for i in d.values():
    if(i not in d.keys()):
        print(i)
