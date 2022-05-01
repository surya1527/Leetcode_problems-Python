nums1 = [12,28,46,32,50] 
nums2 = [50,12,32,46,28]
ans=[]
for i in range(len(nums1)):
    
    for j in range(len(nums2)):
        
        if nums1[i]==nums2[j]:
            ans.append(j)
            break
print(ans)



        
