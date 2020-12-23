from prettytable import PrettyTable

#print table at position t
def printTable(t):
    #remember that the first line of each table are field titles
    ptable = PrettyTable( myList[t][0] )
    for j in myList[t]:
        ptable.add_row(j)
    ptable.del_row(0)
    print(tablenames[t])
    print(ptable)

def showMenu():
    print("OPTIONS:")
    print("1.ADD TABLE")
    print("2.PRINT TABLE")
    print("3.EDIT TABLE")
    print("4.EXIT")

myList = list()
#table counter
t=0
#line counter
l=0

#use this table to store table names
#also usefull for indexes
tablenames =list()

print("Welcome to your database")
showMenu()
menu_answer=input("Select one of the above options: ")

while(menu_answer != "4"):
    
    if(menu_answer == "1"):
    #ADD NEW TABLE
        t = len(tablenames)
        l=0
        a= input("Give a name to your table: ")
        tablenames.append(a)
        #creates table
        myList.append(list())
        myList[t].append(list())
        #dummy variable

        a=""
        while ( a != "STOP" ) :
            a = input("Enter field name or STOP for exit: ")
            if ( a != "STOP"):
                myList[t][l].append(a)

        a = input("Add instance?(y/n): ")
        while(a == "y") :
            l=l+1
            myList[t].append(list())
            for j in myList[t][0]:
                myList[t][l].append(input(j+": "))
            a = input("Add instance?(y/n): ")
        printTable(t)
    
    elif(menu_answer =="2"):
    #PRINT TABLE 
        ptable = PrettyTable(tablenames)
        print(ptable)
        a = input("Type table name to print: ")
        found = False
        for j in tablenames:
            if j == a :
                found=True
        if(found == True):
            t = tablenames.index(a)
            printTable(t)
        else:
            print("There is not such table, try again")
    
    else:
        print("Wrong input, try again")

    showMenu()
    menu_answer=input("Select one of the above options: ")