import csv, time, random
#open the data
with open("laptops.csv", "r") as read:
    data = list(csv.DictReader(read))

company = []
inches = []
resolution = []
cpu = []
ram = []
memory = []
gpu = []
OS = []

for i in data:
    com = i["Company"]
    inc = i["Inches"]
    res = i["ScreenResolution"]
    cp = i["Cpu"]
    mem = i["Memory"]
    ra = i["Ram"]
    gp = i["Gpu"]
    os = i["OpSys"]
    if (not (com in company)): company.append(com)
    if (not (inc in inches)): inches.append(inc)
    if (not (res in resolution)): resolution.append(res)
    if (not (cp in cpu)): cpu.append(cp)
    if (not (mem in memory)): memory.append(mem)
    if (not (ra in ram)): ram.append(ra)
    if (not (gp in gpu)): gpu.append(gp)
    if (not (os in OS)): OS.append(os)

    
def choice(theListName, theListComponent):
    toReturn = dict()
    for i in range(len(theListName)):
        index = 0
        for a in theListComponent[i]:
            print(str(index)+". "+a)
            index+=1
        toReturn[theListName[i]] = theListComponent[i][int(input("What is the %s: "%(theListName[i])))]
        #toReturn[theListName[i]] = theListComponent[i][random.randrange(start=0, stop=len(theListName))]
        #toReturn[theListName[i]] = theListComponent[i][4]
        print("\n\n")
    return toReturn

listName = ["Company", "Inches", "ScreenResolution", "Cpu", "Memory", "Ram", "Gpu", "OpSys"]
inp = choice(listName, [company, inches, resolution, cpu, memory, ram, gpu, OS])
print("Your input: %s\n\n"%(str(inp)))

def firstAlgorithm(listNm):
    poss_price = []
    for a in data:
        for i in range(len(listNm)):
            name = listName[i]
            spec = inp[name]
            if (a[name]==spec):
                poss_price.append(float(a["Price_euros"]))
    real_price = sum(poss_price[i] for i in range(len(poss_price)))/len(poss_price);
    return real_price

def secondAlgorithm():
    #looking for the most significant comparation
    most_significant = ["" for i in range(len(inp))] #it will be the list of spec
    compare_percent = 0
    real_price = 0
    
    for a in data:
        compare_percent_temp = 0
        for i in inp:
            dat = a[i]
            hu = inp[i]
            if (dat==hu):
                compare_percent_temp += 100/len(inp)
                
        if (compare_percent_temp > compare_percent):
            #if its 100% same, then just return the price.
            if (compare_percent_temp==100):
                return a["Price_euros"]
            
            compare_percent = compare_percent_temp
            most_significant = a
    
    #seeking for the missing spec match
    key_to_seek = []
    inp_key = list(inp)
    ms_key = list(most_significant)
    for i in range(len(inp)):
        a = inp[inp_key[i]]
        b = most_significant[ms_key[i]]
        if (not (b==a)):
            key_to_seek.append(inp_key[i])
    print("Most significant: ", most_significant)
    print("with percentage: ", compare_percent)
    
    #the rest of non-match percentage, will be done with firstAlgorithm
    return (float(most_significant["Price_euros"])+ firstAlgorithm(key_to_seek))/2
def thirdAlgorithm(lName):
    
    pass
#print(secondAlgorithm())
print(firstAlgorithm(listName))