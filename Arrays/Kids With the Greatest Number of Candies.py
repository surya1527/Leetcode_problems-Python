candies = [2,3,5,1,3] 
extraCandies = 3
max_can = max(candies)
ans = []
for i in range(len(candies)):
    x = candies[i] + extraCandies
    if x>= max_can:
        ans.append(True)

    else:
        ans.append(False)
print(ans)
