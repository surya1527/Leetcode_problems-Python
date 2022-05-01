s = "aeiou"
vowels =["a", "e", "i", "o", "u"]
res = ""
for i in s:
    if i not in vowels:
        res+=i

print(res)