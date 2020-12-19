f = open("input.txt", "r")
# f = open("example.txt", "r")
inp = f.readlines()
f.close()

# part 1
import math

class Boat:
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.ang = 0
    
    def e(self,d):
        self.posx = self.posx +d
    def w(self,d):
        self.posx = self.posx -d
    def n(self,d):
        self.posy = self.posy +d
    def s(self,d):
        self.posy = self.posy -d
    def rl(self,anAng):
        self.ang = self.ang + anAng
    def rr(self,anAng):
        self.ang = self.ang - anAng
    def f(self,d):
        self.posx = self.posx + round(d*math.cos(self.ang/180*math.pi))
        self.posy = self.posy + round(d*math.sin(self.ang/180*math.pi))
        
    def doCmd(self,cmd,val):
        if cmd == 'N':
            self.n(val)
        elif cmd == 'S':
            self.s(val)
        elif cmd == 'E':
            self.e(val)
        elif cmd == 'W':
            self.w(val)
        elif cmd == 'R':
            self.rr(val)
        elif cmd == 'L':
            self.rl(val)
        elif cmd == 'F':
            self.f(val)
            
# part 2
class BoatWithWayPoint:
    def __init__(self):
        # waypoint relative to ship pos
        self.wpx = 10
        self.wpy = 1
        # ship pos
        self.posx = 0
        self.posy = 0
    
    def doCmd(self,cmd,val):
        if cmd == 'N':
            self.n(val)
        elif cmd == 'S':
            self.s(val)
        elif cmd == 'E':
            self.e(val)
        elif cmd == 'W':
            self.w(val)
        elif cmd == 'R':
            self.rr(val)
        elif cmd == 'L':
            self.rl(val)
        elif cmd == 'F':
            self.f(val)

    def e(self,d):
        self.wpx = self.wpx +d
    def w(self,d):
        self.wpx = self.wpx -d
    def n(self,d):
        self.wpy = self.wpy +d
    def s(self,d):
        self.wpy = self.wpy -d
    def rl(self,anAng):
        myXold = self.wpx
        self.wpx = myXold * round(math.cos(anAng/180*math.pi)) - self.wpy * round(math.sin(anAng/180*math.pi))
        self.wpy = myXold * round(math.sin(anAng/180*math.pi)) + self.wpy * round(math.cos(anAng/180*math.pi))
    def rr(self,anAng):
        myXold = self.wpx
        self.wpx = myXold * round(math.cos(anAng/180*math.pi)) + self.wpy * round(math.sin(anAng/180*math.pi))
        self.wpy =-myXold * round(math.sin(anAng/180*math.pi)) + self.wpy * round(math.cos(anAng/180*math.pi))
    def f(self,d):
        self.posx = self.posx + d * self.wpx
        self.posy = self.posy + d * self.wpy

# b = Boat()
b = BoatWithWayPoint()
for i in range(len(inp)):
    cmd = inp[i][0]
    val = int(inp[i][1:-1])
    # print(inp[i],cmd,val)
    b.doCmd(cmd,val)
    # print(b.posx,b.posy,b.ang)
    # print(b.posx,b.posy,b.wpx,b.wpy)

print(b.posx,b.posy)
print(abs(b.posx)+abs(b.posy))


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        