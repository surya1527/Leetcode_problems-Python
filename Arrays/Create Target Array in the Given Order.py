nums = [0,1,2,3,4] 
index = [0,1,2,2,1]
# res = []
# m = {}
# for i,j in zip(range(len(nums)),index):
#     m[i] = j

# for i in m:
#     res.append(i[0])

# print(m)
# print(res)

x=[]
        
        
for i in range(0,len(nums)):
    
    x.insert(index[i], nums[i])

    
print(x) 