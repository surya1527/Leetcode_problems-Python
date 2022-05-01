sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
a = 0
for i in sentences:
    words = i.split(" ")
    if len(words)>a:
        a = len(words)

print(a)