f = open("input.txt", "r")
# f = open("example.txt", "r")
inp = f.readlines()
f.close()

# part 1
preambleLength = 25
prevSeq = []
for i in range(preambleLength):
    prevSeq.append(int(inp[i][:-1]))

def checkValidity(prevSeq,nr):
    isValid = False
    for i in range(len(prevSeq)):
        for j in range(len(prevSeq)):
            if( i != j and prevSeq[i]+prevSeq[j] == nr):
                isValid = True
                return [isValid, prevSeq[i], prevSeq[j]]
    return [isValid]

foundInvalid = False
for i in range(preambleLength,len(inp)):
    curIn = int(inp[i][:-1])
    ans = checkValidity(prevSeq,curIn)
    if(ans[0] == True):
        prevSeq.pop(0)
        prevSeq.append(curIn)
    elif ans[0] == False and foundInvalid == False:
        foundInvalid = True
        invIdx = i
        invVal = curIn
    
print(invVal)

# part 2
nrs = []
total = 0
minIdx = 0
maxIdx = 0
while total != invVal:
    nrs.append(int(inp[maxIdx][:-1]))
    total = sum(nrs)
    maxIdx = maxIdx + 1
    if(total > invVal):
        minIdx = minIdx +1
        maxIdx = minIdx
        nrs = []
        total = 0
minVal = min(nrs)
maxVal = max(nrs)
print(minVal+maxVal)






