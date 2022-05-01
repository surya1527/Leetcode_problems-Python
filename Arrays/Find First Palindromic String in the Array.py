words = ["abc","car","ada","racecar","cool"]
s = ""
for i in words:
    if i == i[::-1]:
        s+=i
        break
print(s)