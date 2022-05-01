words = ["gin","zen","gig","msg"]

morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

res=[]
for i in words:
    x=""
    for j in i:
        
        index=ord(j)-97
        x+= morse_code[index]
    if x not in res:
        res.append(x)

print(len(res))