jwels = 'z'
stones = 'ZZ'
count = 0
for i in stones:
    for j in jwels:
        if i == j:
            count+=1
            break

print(count)