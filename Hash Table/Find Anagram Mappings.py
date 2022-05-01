from operator import index
from textwrap import indent


nums1 = [40,40]
nums2 = [40,40]


x=[]
for i in range(len(nums1)):
    
    for j in range(len(nums2)):
        
        if nums1[i]==nums2[j]:
            x.append(j)
            break
print(x)