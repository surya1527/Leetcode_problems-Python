nums = [3,1,2,2,2,1,3]
k = 2
count = 0
for i in range(len(nums)):
    for j in range(0,i):
        if nums[i] == nums[j] and (i*j)%k == 0:
            count+=1
print(count)