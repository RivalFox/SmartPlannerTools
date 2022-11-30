
#There should be two lists
#One for computer science electives
#One for general electives

def InferenceEngine(list1,database1):
    #list1 will be the list of students interests
    #need to take a file path for rules
    #rule will be saved up in the text file.

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

    #If list is empty then just add all 6 subjects into the list 
    #if list1 ==

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

    global finalCslist
    finalCslist={}
    global finalGlist
    finalGlist={}

    #check the database and grab all the classes related to interests
    for key, value in DatabaseDict.items():
        #General electives
        for i in range(len(searchList)):
            if key[0:4] == searchList[i]:
                #All the classes need to be put into a electiveslist
                electiveslist[key] = value
        #CS electives
        for i in range(len(searchCSlist)):
             if key[0:4] == searchCSlist[i]:
                #All the classes need to be put into a csElectiveslist
                csElectiveslist[key] = value
       

            
    #Need to create rule text file and save all the rules 
    #Inference engine will read the text file for the rules 
    #Based on that rules, it will give weight on each courses
    #Then, the inference engine will organize the courses in order. 

    #now I need to create rules (Knowledge database)
    #take two lists onr for general list and one for cs list 
        
    #before go through the if statements 
    # 1. Go through the core class list and if it is one of them
    #    electives cannot be chosen as elective
    #    remove all the classes if they are considered as core classes for the major
    # just put it into inference engine (this does not count as rules)
    #Rules are only about (AI)
    coreCSList= ["MATH 1113", "CPSC 1301K", "MATH 2125", "CPSC 1302","CYBR 2159","CYBR 2106" , 
               "CPSC 2105", "MATH 5125", "CPSC 2108", "CPSC 3131","CPSC 5157","CPSC 3121" , 
               "CPSC 5115", "CPSC 3175", "CPSC 3125", "CPSC 5175", "CPSC 5155", "CPSC 5128", 
               "CPSC 5135", "CPSC 4175", "CPSC 4176"]
    
    deleteList=[]
    #Go through the coreCSList and save the core classes
    #from the cs elective list
    for key, value in csElectiveslist.items():
        if key in coreCSList:
            #size is changed during the iteration
            deleteList.append(key)

    #delete the core classes from the cs elective list
    for i in range(len(deleteList)):
        csElectiveslist.pop(deleteList[i])



    #####################getting rule text file#######################
    #The rule text file should be saved in knowledgeDatabase folder
    #open rule file 

    
    # string to search in file
    word = 'RULE'

    ##################################################
    #has to modify path in order to work on any computer
    ##################################################
    #modify in the function too
    ##################################################

    with open(r'.\KnowledgeDatabase\Rules.txt', 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        for line in lines:
            # check if string present on a current line
            if line.find(word) != -1:

                words = line.split()

                for key in csElectiveslist:
                    #key[0:4] = CPSC or CYBR in possible list
                    #words[1]= CPSC or CYBR in rule file
                    if key[0:4]==words[1]:
                        
                        if key[5:6]==words[2]:
                            #Need to add weight value to each course
                            #Put in a new cs elective list with weight
                            
                            csElectiveslist[key]["weight"] = words[4]

                            #problem is that I am getting all same value for everything

                        if key[5:6]==words[2]:
                            #Put in a new cs elective list with weight
                            #Put in a new cs elective list with weight
                            csElectiveslist[key]["weight"] = words[4]

                #Apply same thing for general elective list too
                for key in electiveslist:
                    #key[0:4] = CPSC or CYBR in possible list
                    #words[1]= CPSC or CYBR in rule file
                    if key[0:4]==words[1]:
                        
                        if key[5:6]==words[2]:
                            #Need to add weight value to each course
                            #print("3000 level course: ",key)
                            #Put in a new cs elective list with weight
                            
                            electiveslist[key]["weight"] = words[4]

                            #problem is that I am getting all same value for everything

                        if key[5:6]==words[2]:
                            #Put in a new cs elective list with weight
                            #print("4000 level course: ",key)
                            #Put in a new cs elective list with weight
                            electiveslist[key]["weight"] = words[4]


    #*******next step****************
    #You can get the courses with weight but Prereq
    #################################
    for key, value in csElectiveslist.items():
        #You can get the courses only with weight
        if csElectiveslist[key].get("weight")==None:
            continue
        else:
            #Here I can get courses that has weight but prereq
            if csElectiveslist[key].get("Prerequisite")==None:
                finalCslist[key]=value

    for key, value in electiveslist.items():
        #You can get the courses only with weight
        if electiveslist[key].get("weight")==None:
            continue

        else:
            #Here I can get courses that has weight but prereq
            if electiveslist[key].get("Prerequisite")==None:
                finalGlist[key]=value




    #if there is weight already, then add new weight/2 
    #constantly update it 
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

    return finalGlist, finalCslist
   
