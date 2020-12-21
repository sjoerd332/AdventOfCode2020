f = open("input.txt", "r")
# f = open("example.txt", "r")
inp = f.readlines()
f.close()

# part 1 

class Memory:
    def __init__(self):
        self.memory = []
        self.oneMask = 0
        self.zeroMask = 0
    
    def setMask(self, mask):
        self.zeroMask = 0
        self.oneMask = 0
        for i in reversed(range(len(mask))):
            m = mask[i]
            if m == '0':
                self.zeroMask = self.zeroMask | 2**(len(mask)-i-1)
            elif m == '1':
                self.oneMask = self.oneMask | 2**(len(mask)-i-1)
            # print(i,m,self.oneMask,self.zeroMask)
    
    def writeMemory(self, address, value):
        while address > len(self.memory)-1:
            self.memory.append(0)
        
        if value > 2**36-1 or value < 0:
            a = 1/0
        
        value = (value | self.oneMask)
        value = (value & ~self.zeroMask)
        self.memory[address] = value
        
    def sumMemory(self):
        return sum(self.memory)
    
m = Memory()

for i in range(len(inp)):
    cmd = inp[i][:-1]
    if(cmd.find('mask') != -1):
        m.setMask(cmd[7:])
    else:
        m.writeMemory(int(cmd[cmd.find('[')+1:cmd.find(']')]), int(cmd[cmd.find('=')+2:]))
print(m.sumMemory())
    