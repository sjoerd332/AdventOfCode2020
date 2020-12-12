f = open("input.txt", "r")
# f = open("example.txt", "r")
inp = f.readlines()
f.close()

# part 1

def str2nr(zeroId, oneId, str):
    l = len(str)
    val = 0
    for i in range(l):
        if(str[i] == oneId):
            val = val + 2**(l-i-1)
        
    return val

rows = []
seats = []    
ids = []
maxId = 0
for i in range(len(inp)):
    rows.append(str2nr('F','B',inp[i][:7]))
    seats.append(str2nr('L','R',inp[i][7:10]))
    ids.append(rows[i]*8+seats[i])
    if(ids[i] > maxId):
        maxId = ids[i]

## part 2

ids.sort()
mySeat = 0
for i in range(1,len(ids)):
    if(ids[i] - ids[i-1]>1):
        mySeat = ids[i] -1







