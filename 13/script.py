# f = open("input.txt", "r")
f = open("example.txt", "r")
inp = f.readlines()
f.close()

import math

tstart = int(inp[0][:-1])
def getBusses():
    lastComma = 0
    busses = []
    orderNrs = []
    busCnt = 0
    for i in range(len(inp[1])):
        comma = inp[1][i:-1].find(',')
        if(comma == -1) :
            comma = len(inp[1])
        if(i + comma > lastComma):
            busCnt += 1
            bus = inp[1][i:i+comma]
            if(bus != 'x'):
                busses.append(int(bus))
                orderNrs.append(busCnt-1)
            lastComma = i + comma
        if comma == len(inp[1]):
            return [busses, orderNrs]

# part 1
[b, orderNrs] = getBusses()
firstNrs = []
minTimes = []
for i in range(len(b)):
    firstNr = math.ceil(tstart / b[i]) * b[i]
    firstNrs.append(firstNr)
    minTimes.append(firstNr-tstart)

minWaitTime = min(minTimes)
out1 =  b[minTimes.index(minWaitTime)] * minWaitTime

# part 2

# too long calculation try
# def isMultiple(bigNr, divisor):
#     return bigNr % divisor == 0
# 
# found = False
# i = 0
# minInc = min(b)
# combisFound = 1
# while found == False:
#     i = i + minInc
#     intermediateFound = True
#     for j in range(combisFound-1,len(b)):
#         multiple = isMultiple(i+orderNrs[j],b[j])
#         intermediateFound = intermediateFound and multiple
#         if multiple and j == combisFound:
#             combisFound = combisFound +1
# #             minInc = i
#     if intermediateFound:
#         found = True


# with help: note that numbers are (co) prime
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Existence_(constructive_proof)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b//a) * x, x)
        
a = orderNrs
n = b

# a*x + b*y = gcd(a,b)
gcd, x, y = egcd(n[0], n[1])
X =  a[0] * x * n[0] + a[0] * y * n[1]
# solve m1*n1 + m2*n2 = 1 by extended euclidean algorithm

    
    
    
    
    
    
    
    
    
    