f = open("input.txt", "r")
# f = open("example.txt", "r")
inp = f.readlines()
f.close()

# part 1

# fill passports
grps = [[]]
uniques = []
for i in range(len(inp)):
    if(inp[i] != '\n'):
        for j in range(len(inp[i])-1):
            grps[-1].append(inp[i][j])
    else:
        uniques.append(set(grps[-1]))
        grps.append([])
uniques.append(set(grps[-1]))

sum = 0 
for i in range(len(uniques)):
    sum = sum + len(uniques[i])

## part 2
allHave = inp[0][:-1]
allGrps = []
for i in range(len(inp)):
    if(inp[i] != '\n'):
        for j in range(len(inp[i])-1):
            if(allHave.find(inp[i][j]) == -1):
                allHave = allHave.replace(inp[i][j],'')
        replaceChars = []
        for j in range(len(allHave)):
            if(inp[i].find(allHave[j]) == -1):
                replaceChars.append(allHave[j])
        for j in range(len(replaceChars)):
            allHave = allHave.replace(replaceChars[j],'')
    else:
        allGrps.append(allHave)
        allHave = inp[i+1][:-1]
allGrps.append(allHave)
# print(allGrps)
sum2 = 0
for i in range(len(allGrps)):
    sum2 = sum2 + len(allGrps[i])
    