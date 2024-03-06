#-----------------VARIABLES-----------------
    #f1       : algorithm.txt file in algorithm folder
    #f2       : create record file in record folder
    #spaceList: read the file and get the values
    #table    :data export from algorithm.py




def display(table):

#open algorithm.txt file in algorithm folder
#create the display file in record folder
#get table from algorithm.py and create the text file
#after then print the record

    #open algorithm.txt file or read only
    f1 = open("algorithm/algorithm.txt", "r")

    #get data from algorithm.txt
    spaceList = f1.readline()
    f1.close()

    #display the record and write it on a text file
    for a in range((len(table[0].split(",")))-1):
        for b in range(len(table)): 
        
            print((table[b].split(","))[a],end="\t") 


            #open the text file and store the records
            f2 = open("record/" + spaceList + ".txt", "a+")
            f2.write(str((table[b].split(","))[a]+"\t"))

            #open algorithm.txt file and updating
            f1 = open("algorithm/algorithm.txt", "w")
            f1.write(str(int(spaceList) + 1))

    
        print()
        f2.write("\n")
        f2.close()
    print("\n*Your Record Save in ")
    print("\n\tRecord: DOC334_CW_2019784 -----> record ----->",spaceList,".txt file")

    #import ht.py file in htmlcode folder
    from htmlcode.html import html

    #calling html def in html.py
    html()


