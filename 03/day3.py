f = open("input.txt", "r")
# f = open("example.txt", "r")
inp = f.readlines()
f.close()

# part 1
def calcNrOfTrees(stepsToRight, stepsToBottom):
    ypos = 0
    xpos = 0
    treesHit = 0
    height = len(inp)-1
    width = len(inp[0])
    while(ypos < height):
        ypos = (ypos + stepsToBottom)
        xpos = (xpos + stepsToRight) % (width-1)
        if(inp[ypos][xpos] == '#'):
            treesHit = treesHit +1
    return treesHit

ans1 = calcNrOfTrees(3,1)

#part 2
routeTrees = []
routeTrees.append(calcNrOfTrees(1,1))
routeTrees.append(calcNrOfTrees(3,1))
routeTrees.append(calcNrOfTrees(5,1))
routeTrees.append(calcNrOfTrees(7,1))
routeTrees.append(calcNrOfTrees(1,2))

ans2 = 1
for i in range(len(routeTrees)):
    ans2 = ans2*routeTrees[i]