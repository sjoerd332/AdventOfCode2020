f = open("input.txt", "r")
# f = open("example.txt", "r")
inp = f.readlines()
f.close()

# part 1

class Processor():
    def __init__(self):
        self.reset()
        self.progMem = []
    
    def reset(self):
        self.pc = 0
        self.acc = 0
        self.doneOps = []
        self.repFlag = False
        
    
    def loadProgram(self, aProgram):
        for i in range(len(aProgram)):
            op = aProgram[i][:3]
            arg = int(aProgram[i][4:-1])
            self.progMem.append({'op':op,'arg':arg})
    
    def doStep(self):
        op = self.progMem[self.pc]['op']
        arg = self.progMem[self.pc]['arg']
        # log 
        if((self.pc in self.doneOps) == False):
            self.doneOps.append(self.pc)
        else:
            self.repFlag = True
            return
        
        # perform action
        if(op == 'acc'):
            self.acc = self.acc + arg
        elif(op == 'jmp'):
            self.pc = self.pc + arg
        elif(op == 'nop'):
            pass
            
        if(op != 'jmp'):
            self.pc = self.pc +1
        
    def run(self):
        while(self.pc != len(self.progMem)):
            self.doStep()
            
    def runTilRepetition(self):
        while(self.repFlag == False):
            self.doStep()
    
    def changeNopOrJmpUntilEnd(self):
        opNr = -1
        while(self.pc != len(self.progMem)-1):
            self.reset()
            # find next nop or jmp
            foundNext = 0
            for i in range(opNr+1,len(self.progMem)-1):
                op = self.progMem[i]['op']
                arg = self.progMem[i]['arg']
                if((op == 'jmp' or op == 'nop') and foundNext ==  False):
                    if(op == 'jmp'):
                        opNr = i
                        self.progMem[opNr]['op'] = 'nop'
                        foundNext = True
                    elif(op == 'nop' and arg != 0):
                        opNr = i
                        self.progMem[opNr]['op'] = 'jmp'
                        foundNext = True
            # try to execute untill end
            while(self.pc != len(self.progMem) and self.repFlag == False):
                self.doStep()
            if(self.pc == len(self.progMem)):
                return
            # reset changed instr
            op = self.progMem[opNr]['op']
            arg = self.progMem[opNr]['arg']
            if(op == 'jmp'):
                self.progMem[opNr]['op'] = 'nop'
            elif(op == 'nop' and arg != 0):
                self.progMem[opNr]['op'] = 'jmp' 
            
p = Processor()
p.loadProgram(inp)

#part 1
# p.runTilRepetition()
# print(p.acc)

#part 2
p.changeNopOrJmpUntilEnd()















