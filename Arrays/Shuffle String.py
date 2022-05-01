s = "codeleet" 
indices = [4,5,6,7,0,2,1,3]
ans=''
m={}
for i,c in zip(indices,s):
    m[i]=c
for i in sorted(m.items()):
    ans+=i[1]
print(ans) 
