nums = [0,1,2,3,4] 
index = [0,1,2,2,1]

x=[]

for i in range(0,len(nums)):
    x.insert(index[i], nums[i])
print(x) 
