arr = [1,4,2,5,3]
count = 0
for i in range(len(arr)):
    for j in range(len(arr) + 1):
        sliced = arr[:j]
        if len(sliced) % 2 == 1:
            count += sum(sliced)

        if j == len(arr):
            arr.pop(0)

print(count)






