
#There should be two lists
#One for computer science electives
#One for general electives
def InferenceEngine(list1,database1):
    
    #database1 is class information database
    DatabaseDict = database1
   
    ##Need to have another list for computer sciecne electives##

    ##########This is for general electives#####################
    ##**No journalism (need to be deleted in GUI)**##
    #"Psychology"  = PSYC
    #"Statistics"  = STAT
    #"Kinesiology" = KINS
    #"Geology"     = GEOL
    #"Art History" = ARTH
    #"Finance"     = FINC

    #convert the list from string to 4digits and save it into searchList
    searchList=[]
    for i in range(len(list1)):
        if list1[i] == "Psychology":
            searchList.append("PSYC")

        if list1[i] == "Statistics":
            searchList.append("STAT")

        if list1[i] == "Kinesiology":
            searchList.append("KINS")

        if list1[i] == "Geology":
            searchList.append("GEOL")
        
        if list1[i] == "Art History":
            searchList.append("ARTH")

        if list1[i] == "Finance":
            searchList.append("FINC")

    #Hold all the electives that are related to students interests
    #This dictionary hold data
    global electiveslist
    electiveslist= {}
    #Class database
    searchCSlist= ["CPSC", "CYBR"]
    global csElectiveslist
    csElectiveslist={}
    for i in range(len(searchList)):
        print(searchList[i])

    #check the database and grab all the classes related to interests
    for key, value in DatabaseDict.items():
        #General electives
        for i in range(len(searchList)):
            if key[0:4] == searchList[i]:
                #print (key, value)
                #All the classes need to be put into a electiveslist
                electiveslist[key] = value
        #CS electives
        for i in range(len(searchCSlist)):
             if key[0:4] == searchCSlist[i]:
                #All the classes need to be put into a csElectiveslist
                csElectiveslist[key] = value
       

    #Print general elective list
    for key, value in electiveslist.items():
        print(key,value)
    #Print compute sciecne elective list
    for key, value in csElectiveslist.items():
        print(key,value)
    

    #**What kinds of electives the Computer science major students need to take?**
    
    
    #now I need to create rules (Knowledge database)
    def rules (dictlist):
        

        #before go through the if statements
        # 1. Go through the core class list and if it is one of them
        #    electives cannot be chosen as elective
        #    remove all the classes if they are considered as core classes for the major
        coreCSList= ["MATH 1113", "CPSC 1301K", "MATH 2125", "CPSC 1302","CYBR 2159","CYBR 2106" , 
                   "CPSC 2105", "MATH 5125", "CPSC 2108", "CPSC 3131","CPSC 5157","CPSC 3121" , 
                   "CPSC 5115", "CPSC 3175", "CPSC 3125", "CPSC 5175", "CPSC 5155", "CPSC 5128", 
                   "CPSC 5135", "CPSC 4175", "CPSC 4176"]
        #go through the rules and give the each class confidence score (weight)
        #Recommend CPSC and CYBR classes 3000 level other than core classes
        
        #1.core class should not be recommended as CS electives
        #these classes will have 0 weight 

        
        

        #1st interest should have higher weight then 2nd, 2nd higher than 3rd. 
        #if student is freshmen, choose 1000 lvl electives
        #if student is sophomore and junior, choose 2000 lvl electives
        #if student is  senior, choose 3000 lvl electives
        #if the class has the prereq, then give 0 weight. so IE does not choose.

        #another function takes the electivesList
        #Go through all the if, then statements 
        #give each class different weight based on the information
    
        #based on the above results, put electives in the list in order
        #add elective with higher score to the list first in order. 

        return list

    #getter for elective list
    def getElectiveList():
        #returns a dictionary
        return electiveslist
    #getter for cs elective list
    def getCSelectiveList():
        return csElectiveslist
   







