
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
max_num = 0

for i in sentences:
    words = i.split(' ')
    if len(words) > max_num:
        max_num = len(words)

print(max_num)
