#------------------VARIABLES-------------------
    # a,b      : using this variables as count in "for" loop
    # rntc     : to get the random numbers
    # spaceList: (10 - 100) list with given a space
    # numList  : (10 - 100) number list
    # table    : to get final value table
    # blank    : using for search a space in "rntc"
    # value_2  : coming from the perc.py file


import random
import sys
sys.path.insert(0,'displayRecord')
import sheet


def space(value_2,rntc):
    
#if 'rntc'(random number table column) have a space then this def works
#adding numbers to the table column (rntc)
#creating the final table in 'table'

    #creating the columns
    for a in range(value_2): 

        #search spaces and stop data duplication
        if " " in rntc: 
            rntc += (random.choice(numList) + ",")

        else:
            rntc += (random.choice(spaceList) + ",")


        #search column and insert "NO" or "OK"
        if a == value_2 - 1: 
                if " " in rntc:
                    rntc += ("NO,")

                else:
                    rntc += ("OK,")

    table.append(rntc)
    

def nospace(value_2,rntc):
    
#if rntc(random numbers table column) have not a space then this def works
#adding numbers to random numbers table column(rntc)
#creating the final table(table)


    #creating the columns
    for a in range(value_2): 

        #adding the numbers
        rntc += (random.choice(numList) + ",")

        #insert "NO" and "OK"
        if a == value_2 - 1:
            if " " in rntc: 
                rntc += ("NO,")

            else:
                rntc += ("OK,")

    table.append(rntc)
   

def randwork(value_1,value_2):

#create 'spaceList' and 'numList' list
#search space in the random number table column 'rntc'
#stoping the space duplcation(again and again)


    global numList
    global spaceList
    global table


    table = []
    spaceList = [" ", ]
    numList = []
    blank = 0

    #create 'spaceList' and 'numList' lists
    for a in range(10, 100): 
        spaceList.append(str(a))
        numList.append(str(a))

    #creating the table rows
    for b in range(value_1): 

    #stoping the space duplcation(again and again) 

        #asking the space def
        if blank == 0:
            rntc = ""
            space(value_2,rntc)
            blank = 1

        #asking the nospace def
        else:
            rntc = ""
            nospace(value_2,rntc)
            blank = 0

    #print(table)
    sheet.display(table)
    
