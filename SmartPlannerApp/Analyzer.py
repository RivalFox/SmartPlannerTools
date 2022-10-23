InputDict = {}
    
def analyzeData(path, filename, database):
    global InputDict
    # Open and Read File
    inputFile = open(path + "\\" + filename)
    DatabaseDict = database
    InputDict = {}
    #classList = []
    phrase = "Needed"
    #count = 0
    for line in inputFile:
        #Finds the line that contains the phrase "Needed"
        if line.find(phrase) != -1: 
            #Once found, moves onto the next line
            nextLine = next(inputFile)
            for word in nextLine.split():

                if word.isupper() and len(word) == 4:
                    #print(word)

                    for num in nextLine.split():
                        if num[0].isdigit() and len(num) > 3:
                         #print(word + " " + num[:4])
                         #classList.append(word + " " + num[:4])
                         className = word + " " + num[:4]

                         InputDict[className] = {}
                         InputDict[className]["Name"] = className
                         #Dictionary[word + " " + num[:4]]["Name"] = {}


    #print(classList)
    for key, value in DatabaseDict.items():
        t = InputDict.get(key)
        if t != None:
            InputDict[key] = value
        #else:
            #print("")

    List = []
    for key, value in InputDict.items():
        if InputDict[key].get("Credits") == None:
            List.append(key)
        #print(key, ":", value)

    for i in range(len(List)):
        InputDict.pop(List[i])
        #print(List[i], " has been popped")


def getInputDatabase():
    return InputDict
    #inputFile.close()






    ##Check if a certain class has pre-req classes##