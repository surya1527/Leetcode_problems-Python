nums = [1,2,3,4]
x=[]
for i in range(0,len(nums),2):
    
    x =x+ ([nums[i+1]]*nums[i])
    
    
print(x)