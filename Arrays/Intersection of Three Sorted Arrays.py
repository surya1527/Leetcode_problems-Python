arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
lis = []
a = set(arr1).intersection(set(arr2))
b = a.intersection(set(arr3))
lis.append(b)
print(sorted(b))