nums = [1,3]
k = 0
count = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if abs(nums[i]- nums[j]) == k :
            count+=1


print(count)