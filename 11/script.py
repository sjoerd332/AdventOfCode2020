f = open("input.txt", "r")
# f = open("example.txt", "r")
inp = f.readlines()
f.close()

for i in range(len(inp)):
    inp[i] = inp[i][:-1]

# part 1 2
def update1(aGrid):
    myGrid = aGrid.copy()
    for i in range(len(aGrid)):
        for j in range(len(aGrid[0])):
            minx = max(0,j-1)
            maxx = min(len(aGrid[0])-1,j+1)
            miny = max(0,i-1)
            maxy = min(len(aGrid)-1,i+1)
            # count occupied surrounding seats
            occupied = 0
            for k in range(miny,maxy+1):
                for l in range(minx,maxx+1):
                    if( not (k == i and l == j) and aGrid[k][l] == '#'):
                        occupied = occupied +1
            if(occupied == 0 and aGrid[i][j] == 'L'):
                myStr = list(myGrid[i])
                myStr[j] = '#'
                myGrid[i] = ''.join(myStr)
            elif(occupied >= 4 and aGrid[i][j] == '#'):
                myStr = list(myGrid[i])
                myStr[j] = 'L'
                myGrid[i] = ''.join(myStr)
    return myGrid
    
def update2(aGrid):
    myGrid = aGrid.copy()
    for i in range(len(aGrid)):
        for j in range(len(aGrid[0])):
            occupied = 0
            # north
            firstSeatFound = False
            for k in reversed(range(0,i)):
                if((aGrid[k][j] == '#' or aGrid[k][j] == 'L') and firstSeatFound == False):
                    firstSeatFound = True
                    if(aGrid[k][j] == '#'):
                        occupied = occupied +1
            # west
            firstSeatFound = False
            for k in reversed(range(0,j)):
                if((aGrid[i][k] == '#' or aGrid[i][k] == 'L') and firstSeatFound == False):
                    firstSeatFound = True
                    if(aGrid[i][k] == '#'):
                        occupied = occupied +1
            # south
            firstSeatFound = False
            for k in range(i+1,len(aGrid)):
                if((aGrid[k][j] == '#' or aGrid[k][j] == 'L') and firstSeatFound == False):
                    firstSeatFound = True
                    if(aGrid[k][j] == '#'):
                        occupied = occupied +1
            # east
            firstSeatFound = False
            for k in range(j+1,len(aGrid[0])):
                if((aGrid[i][k] == '#' or aGrid[i][k] == 'L') and firstSeatFound == False):
                    firstSeatFound = True
                    if(aGrid[i][k] == '#'):
                        occupied = occupied +1
            # north west
            l = min(i,j)
            firstSeatFound = False
            if(l>0):
                for k in range(1,l+1):
                    if((aGrid[i-k][j-k] == '#' or aGrid[i-k][j-k] == 'L') and firstSeatFound == False):
                        firstSeatFound = True
                        if(aGrid[i-k][j-k] == '#'):
                            occupied = occupied +1
            # south west
            l = min(len(aGrid)-1-i,j)
            firstSeatFound = False
            if(l>0):
                for k in range(1,l+1):
                    if((aGrid[i+k][j-k] == '#' or aGrid[i+k][j-k] == 'L') and firstSeatFound == False):
                        firstSeatFound = True
                        if(aGrid[i+k][j-k] == '#'):
                            occupied = occupied +1
            # south east
            l = min(len(aGrid)-1-i,len(aGrid[0])-1-j)
            firstSeatFound = False
            if(l>0):
                for k in range(1,l+1):
                    if((aGrid[i+k][j+k] == '#' or aGrid[i+k][j+k] == 'L') and firstSeatFound == False):
                        firstSeatFound = True
                        if(aGrid[i+k][j+k] == '#'):
                            occupied = occupied +1
            # north east
            l = min(i,len(aGrid[0])-1-j)
            firstSeatFound = False
            if(l>0):
                for k in range(1,l+1):
                    if((aGrid[i-k][j+k] == '#' or aGrid[i-k][j+k] == 'L') and firstSeatFound == False):
                        firstSeatFound = True
                        if(aGrid[i-k][j+k] == '#'):
                            occupied = occupied +1
            if(occupied == 0 and aGrid[i][j] == 'L'):
                myStr = list(myGrid[i])
                myStr[j] = '#'
                myGrid[i] = ''.join(myStr)
            elif(occupied >= 5 and aGrid[i][j] == '#'):
                myStr = list(myGrid[i])
                myStr[j] = 'L'
                myGrid[i] = ''.join(myStr)
    return myGrid

def pGrid(aGrid):
    for i in range(len(aGrid)):
        print(aGrid[i])
    print('\n')
 
pGrid(inp)

oldGrid = []
newGrid = inp
while(oldGrid != newGrid):
    oldGrid = newGrid
    # newGrid = update1(oldGrid)
    newGrid = update2(oldGrid)
pGrid(newGrid)

cnt = 0
for i in range(len(newGrid)):
    for j in range(len(newGrid[0])):
        if(newGrid[i][j] == '#'):
            cnt = cnt+1