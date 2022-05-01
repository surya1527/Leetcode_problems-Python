s = "aaaabbbbcccc"
char_count = {}
for char in s:
    count = char_count.setdefault(char, 0)
    char_count[char] = count + 1             
uniq_s = sorted(list(char_count.keys()))
uniq_s = uniq_s + uniq_s[::-1]

new_s = []
while len(s) - len(new_s) > 0:
    for c in uniq_s:
        if char_count[c] > 0:
            new_s.append(c)
            char_count[c] -= 1

print("".join(new_s))

