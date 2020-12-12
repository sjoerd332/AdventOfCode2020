f = open("input.txt", "r")
# f = open("example.txt", "r")
# f = open("example2.txt", "r")
# f = open("example3.txt", "r")
inp = f.readlines()
f.close()

# part 1

# fill passports
passports = []
passports.append({})
props = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:','cid:']
for i in range(len(inp)):
    if(inp[i] != '\n'):
        #add line to passport
        for j in range(len(props)):
            if(inp[i].find(props[j]) != -1):
                firstPosAfterKey = inp[i].find(props[j])+4
                allSeparators = [x for x in range(len(inp[i])) if (inp[i].startswith(' ', x) or inp[i].startswith('\n', x))]
                breakLoop = False
                for k in range(len(allSeparators)):
                    if(allSeparators[k] - firstPosAfterKey > 0 and breakLoop == False):
                        breakLoop = True
                        firstSepAfterKey = allSeparators[k]
                passports[-1][props[j]] = inp[i][firstPosAfterKey:firstSepAfterKey]
    else:
        passports.append({})


valid = 0
validEntries = []
for i in range(len(passports)):
    x = passports[i]
    if(props[0] in x and props[1] in x and props[2] in x and props[3] in x and props[4] in x and props[5] in x and props[6] in x):
        valid = valid +1
        validEntries.append(i)
        
## part 2
valid2 = 0
valid2Entries = []
invalid2Entries = []
for i in range(len(passports)):
    x = passports[i]
    byrValid = False
    iyrValid = False
    eyrValid = False
    hgtValid = False
    hclValid = False
    eclValid = False
    pidValid = False
    
    if(props[0] in x):
        byr = int(x[props[0]])
        if byr >= 1920 and byr <= 2002:
            byrValid = True

    if(props[1] in x):
        iyr = int(x[props[1]])
        if iyr >= 2010 and iyr <= 2020:
            iyrValid = True
            
    if(props[2] in x):
        eyr = int(x[props[2]])
        if eyr >= 2020 and eyr <= 2030:
            eyrValid = True
            
    if(props[3] in x):
        hgt = x[props[3]]
        if(hgt.find('cm') != -1):
            if(int(hgt[0:-2]) >= 150 and int(hgt[0:-2]) <= 193):
                hgtValid = True
        elif(hgt.find('in') != -1):
            if(int(hgt[0:-2]) >= 59 and int(hgt[0:-2]) <= 76):
                hgtValid = True
                
    if(props[4] in x):
        hcl = x[props[4]]
        if(hcl[0] == '#'):
            try:
                int(hcl[1:],16)
                hclValid = True
            except:
                pass
                
    if(props[5] in x):
        ecl = x[props[5]]
        if(ecl == 'amb' or ecl == 'blu' or ecl == 'brn' or ecl == 'gry' or ecl == 'grn' or ecl == 'hzl' or ecl == 'oth'):
            eclValid = True
            
    if(props[6] in x):
        pid = x[props[6]]
        if(len(pid) == 9):
            try:
                int(pid)
                pidValid = True
            except:
                pass
        
    if(byrValid and iyrValid and eyrValid and hgtValid and hclValid and eclValid and pidValid):
        valid2 = valid2 +1
        valid2Entries.append(i)
    else: 
        invalid2Entries.append(i)
        
    # print(byrValid,iyrValid,eyrValid,hgtValid,hclValid,eclValid,pidValid)


















