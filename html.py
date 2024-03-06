#----------------------VARIABLES------------------------
    #f1       : open algorithm.txt file in algorithm folder
    #spaceList: keep data from file
    #ftitle   : using this to give a name for html code file
    #f2       : open record file in the record folder
    #sf2      : using this to keep data from  f2
    #f3       : create html files in htmlcode/record folder
    #shtml    : using this for keep  html code




def html():

#open files of f1,f2,f3 and acquire data
#write html files

    #open the algorithm.txt file
    f1= open("algorithm/algorithm.txt","r")
    spaceList=f1.readline()

    #search record text file name 
    ftitle=str((int(spaceList))-1)
    f2= open("record/"+ftitle+".txt","r")
    sf2=f2.readlines()

    f3 = open("htmlcode/record/"+(str(int(spaceList)-1))+'.html','a')

    #create html tags on htmlcode file
    shtml = '''<html> <body> <h5> DOC334_CW_2019784/htmlcode/record </h5>
        <h3 align = "Center"> Record </h3>
        <table style="width:40%",align:"Center", border=1 , align="Center">'''

    f3.write(shtml)


    for b in sf2:
        f3.write("<tr align = center>")
        
        blank= b.split("\t")

        for a in range((len(blank))-1):

            f3.write("<td>"+blank[a]+"</td>")       

        f3.write("</tr>")


    shtml = '''

    </table>
    </body>
    </html>'''

    f3.write(shtml)
    f1.close()
    f3.close()
    f2.close()

    print("\n\n*you can follow the web browser to see the record","\n\n",
          "\tRecord Path Direction: DOC334_CW_2019784 -----> htmlcode -----> record"
          +str(int(spaceList)-1)+".html")



