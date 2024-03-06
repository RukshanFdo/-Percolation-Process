#----------------VARIABLES--------------------
   #grid                : argument controlling
   #value_1 and value_2: make use of for get argument first value and second values


from algorithm.algorithm import randwork
import sys
 
#discover the argument length
if len(sys.argv)==1: 
    grid = " "
    
#obtain the last argument    
else:
    grid = sys.argv[-1] #obtain the last argument

#create default value for the code
if grid == " " or grid == " ":
    value_1,value_2 = 5,5 
    randwork(value_1,value_2)

#search for an error
else:
    if int(grid[0])>2 and int(grid[2])>2 and int(grid[0])<10 and int(grid[2])<10:
        value_2,value_1=int(grid[0]),int(grid[2])
        randwork(value_1,value_2)


#display the error message
    else:
        print("\n\t------Your Enter Grid Size is Valid------","\n")
        print("\t\t*Grid 3x3 should be the LOWEST DIMENSIONS for this system")
        print("\t\t*Grid 9x9 should be the HIGHEST DIMENSIONS for this system")
        print("\n\t------Please Correct the Grid Size and Try Again!------")



