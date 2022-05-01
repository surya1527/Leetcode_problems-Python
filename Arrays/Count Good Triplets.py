arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
lis = []
count  = 0
for k in range(len(arr)):
    for j in range(0, k):
        for i in range(0,j):
            if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                count+=1

print(count)
 