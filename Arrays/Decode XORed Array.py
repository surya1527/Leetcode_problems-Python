encoded = [1,2,3] 
first = 1
arr = [first]
for i in range(len(encoded)):
    arr.append(encoded[i]^arr[-1])

print(arr)


