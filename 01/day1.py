f = open("input.txt", "r")
inp = f.readlines()
inpInt = []
for i in range(0,len(inp)):
    inpInt.append(int(inp[i]))

f.close()

for i in range(len(inpInt)):
    for j in range(len(inpInt)):
        if inpInt[i]+inpInt[j] == 2020:
            ansi = i
            ansj = j
            ans = inpInt[i]*inpInt[j]
            break
            
## part 2
class foundIt(Exception):pass
try: 
    for i in range(len(inpInt)):
        for j in range(len(inpInt)):
            for k in range(len(inpInt)):
                if inpInt[i]+inpInt[j]+inpInt[k] == 2020 and i != j and i != k and j != k:
                    ansi = i
                    ansj = j
                    ansk = k
                    ans = inpInt[i]*inpInt[j]*inpInt[k]
                    raise foundIt
except:
    foundIt