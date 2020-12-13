f = open("input.txt", "r")
# f = open("example.txt", "r")
inp = f.readlines()
f.close()

# part 1
myBag = 'shiny gold'

class Bag:
    def __init__(self,aLook,anIsContainedBy=None):
        self.containedBags = []
        self.containedAmount = []
        self.theLook = aLook
        self.theIsContainedBy = anIsContainedBy
    
    def addBagType(self,anAmount, aBag):
        self.containedBags.append(aBag)
        self.containedAmount.append(anAmount)
        
    def containsType(self,aLook):
        for i in range(len(self.containedBags)):
            if(aLook in self.containedBags[i].theLook):
                return True
        return False
        
    def canHoldType(self,aLook):
        myAns = self.containsType(aLook)
        for i in range(len(self.containedBags)):
            myAns = myAns or self.containedBags[i].canHoldType(aLook)
        return myAns
            
    def countInsideBags(self):
        mySum = sum(self.containedAmount)
        for i in range(len(self.containedBags)):
            mySum = mySum + self.containedAmount[i] * self.containedBags[i].countInsideBags()
        return mySum

    def printInfo(self,tabidx):
        print('\t'*tabidx, self.theLook, "has" if len(self.containedBags)>0 else "")
        for i in range(len(self.containedBags)):
            print('\t'*tabidx,'idx ', i,self.containedBags[i].theLook)
            self.containedBags[i].printInfo(tabidx+1)
            
# parse rules
bags = []

for i in range(len(inp)):
    sContain = inp[i].find('contain')-6
    eContain = inp[i].find('contain')+8
    bigBagLook = inp[i][:sContain]
    bags.append(Bag(bigBagLook,None))
    bigBagIdx = len(bags)-1
    separators = []
    separators.append(eContain)
    commas = [x for x in range(len(inp[i])) if (inp[i].startswith(',', x-2))]
    separators.extend(commas)
    separators.append(len(inp[i])-1)
    for j in range(len(separators)-1):
        st = inp[i][separators[j]:separators[j+1]]
        if(st.find('no other') == -1):
            b = st.find('bag')-1
            st = st[:b]
            s = st.find(' ')
            nr = int(st[:s])
            look = st[s+1:]
            a = Bag(look,bags[bigBagIdx].theLook)
            bags[bigBagIdx].addBagType(nr,a)
            bags.append(a)
    
# find root level bags
bagsToRemove = []
for i in range(len(bags)):
    if bags[i].theIsContainedBy == None:
        cnt = 0
        for j in range(len(bags)):
            if j != i and bags[j].theLook == bags[i].theLook:
                # fill entries in other rules by the content of rule i
                bags[j].containedBags = bags[i].containedBags
                bags[j].containedAmount = bags[i].containedAmount
                cnt = cnt +1
        if cnt > 0:
            bagsToRemove.append(bags[i])
for i in reversed(range(len(bagsToRemove))):
    bags.remove(bagsToRemove[i])
    bagsToRemove.pop(-1)

# merge duplicates
for i in range(len(bags)):
    for j in range(len(bags)):
        if j > i and bags[i].theLook == bags[j].theLook:
            bagsToRemove.append(j)
bagsToRemove = list(set(bagsToRemove))
for i in reversed(range(len(bagsToRemove))):
    bags.pop(bagsToRemove[i])
    bagsToRemove.pop(-1)

cnt = 0
for i in range(len(bags)):
    cnt = cnt + bags[i].canHoldType(myBag)
    
# bags[0].printInfo(0)

## part 2
for i in range(len(bags)):
    if(bags[i].theLook == myBag):
        print(bags[i].countInsideBags())





