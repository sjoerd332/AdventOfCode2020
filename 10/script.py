# f = open("input.txt", "r")
# f = open("example.txt", "r")
f = open("example2.txt", "r")
inp = f.readlines()
f.close()

# part 1
joltages = [0]
for i in range(len(inp)):
    joltages.append(int(inp[i][:-1]))
joltages.append(max(joltages)+3)

joltages.sort()
diffs = []
for i in range(1,len(joltages)):
    diffs.append(joltages[i]-joltages[i-1])

prod = diffs.count(1) * diffs.count(3)

# part 2
triples = []
doubles = []
singles = []
prevIsTriple = False
prevIsDouble = False
for i in range(len(diffs)-2):
    if(diffs[i+1] == 1 and diffs[i+2] == 1 and diffs[i+3] == 1 and diffs[i+4] == 1):
        # then three replaceable entries
        triples.append(joltages[i+2])
        prevIsDouble = False
        prevIsTriple = True
    elif(diffs[i+1] == 1 and diffs[i+2] == 1 and diffs[i+3] == 1 and prevIsTriple == False):
        # then two replaceable entries
        doubles.append(joltages[i+2])
        prevIsDouble = True
        prevIsTriple = False
    elif(diffs[i+1] == 1 and diffs[i+2] == 1 and prevIsDouble == False and prevIsTriple == False):
        # then one replacable entries
        singles.append(joltages[i+2])
        prevIsDouble = False
        prevIsTriple = False
    else:
        prevIsDouble = False
        prevIsTriple = False
        
orders = 7*len(triples)*4*len(doubles)*2*len(singles)