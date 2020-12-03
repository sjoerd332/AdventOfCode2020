f = open("input.txt", "r")
inp = f.readlines()
f.close()

# part 1
nrOfCorrectWords = 0
for i in range(0,len(inp)):
    minNr = int(inp[i][0:inp[i].find('-')])
    maxNr = int(inp[i][inp[i].find('-')+1:inp[i].find(' ')])
    char = inp[i][inp[i].find(' ')+1]
    word = inp[i][inp[i].find(':')+1:inp[i].find('\n')]
    count = 0
    for j in word:
        if j == char:
            count = count +1
    if(count >= minNr and count <= maxNr):
        nrOfCorrectWords = nrOfCorrectWords +1

#part 2
nrOfCorrectWords = 0   
for i in range(0,len(inp)):
    nr1 = int(inp[i][0:inp[i].find('-')])
    nr2 = int(inp[i][inp[i].find('-')+1:inp[i].find(' ')])
    char = inp[i][inp[i].find(' ')+1]
    word = inp[i][inp[i].find(':')+1:inp[i].find('\n')] #explicitly include space
    if (word[nr1] == char) != (word[nr2] == char):
        nrOfCorrectWords = nrOfCorrectWords +1