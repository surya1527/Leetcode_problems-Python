rings = "B0B6G0R6R0R6G9R0"
d={}
count = 0
for i in range(1,len(rings),2):
    if rings[i] not in d:
        d[rings[i]]=[rings[i-1]]
    else:
        d[rings[i]].append(rings[i-1])        
for i in d:
    print(d)
    if len(set(d[i]))==3:
        count+=1
print(count)
