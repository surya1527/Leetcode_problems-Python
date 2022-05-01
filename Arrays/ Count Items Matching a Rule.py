items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color" 
ruleValue = "silver"
count = 0
d  = {'type':0,'color':1,'name':2}
for i in items:
    if i[d[ruleKey]] == ruleValue:
        count+=1

print(count)