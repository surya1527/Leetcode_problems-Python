nums = [2,5,1,3,4,7]
n = 3
ans = []

for item1,item2 in zip(nums[0:n],nums[n::]):
    ans.append(item1)
    ans.append(item2)

print(ans)

