arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9] 
arr3 = [1,3,4,5,8]

result = []
for i in range(len(arr1)):
    if arr1[i] in arr2 and arr1[i] in arr3:
        result.append(arr1[i])

print(result)
