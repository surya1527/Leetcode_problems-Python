keyboard = "abcdefghijklmnopqrstuvwxyz"
word = "cba"
sum=0
initial=0
for i in word:
    for j in keyboard:
        if i==j:
            step= keyboard.index(j)
            break
    dif = abs(step-initial)            
    sum += dif
    initial=step
print(sum)