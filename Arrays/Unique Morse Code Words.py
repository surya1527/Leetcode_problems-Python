words = ["gin","zen","gig","msg"]
morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
lis = []

for i in words:
    s = ""
    for j in i:
        index = ord(j)-97
        s += morse_code[ index]
    if s not in lis:
        lis.append(s)

print(len(lis))
