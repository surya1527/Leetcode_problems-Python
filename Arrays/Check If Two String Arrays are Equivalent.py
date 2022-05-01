word1 = ["ab", "c"] 
word2 = ["a", "bc"]
str1 = word1[0]
str2 = word2[0]

for i in range(1,len(word1)):
    str1 += word1[i]
for j in range(1,len(word2)):
    str2 += word2[j]

print(str1 == str2)
