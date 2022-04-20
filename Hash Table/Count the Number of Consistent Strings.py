allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
count = len(words)
for i in words:
    for j in i:
        if j not in allowed:
            count-=1
            break
print(count)
