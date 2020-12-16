f = open("input.txt", "r")
# f = open("example.txt", "r")
# f = open("example2.txt", "r")
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

class CombinationsStore:
    def __init__(self):
        self.combinations = {-1:1}
        self.combinations.update({0:1})
        self.combinations.update({1:2})
        self.combinations.update({2:4})
        self.combinations.update({3:7})
        self.combinations.update({4:10})
        
s = CombinationsStore()

i = 0
combis = 1
while(i < len(diffs)):
    j = 0
    while(diffs[i+j] == 1):
        j = j +1
    combis = combis * s.combinations.get(j-1)
    if(j>0):
        i = i +j
    else:
        i = i +1
print(combis)