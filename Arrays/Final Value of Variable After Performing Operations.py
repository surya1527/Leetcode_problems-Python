operations = ["--X","X++","X++"]
ans = 0
for operation in operations:
    ans = ans + 1 if operation in ["++X","X++"] else ans-1
print(ans) 