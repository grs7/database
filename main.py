from prettytable import PrettyTable

print("welcome to my database")
print("Create list fields")

#all the databse is stored here
myList = list()
myList.append(list())

#position [0...n][0] are field names
#position [0...n][0...n] are field values

#use this to count element line
i=0

#Tablename
tablename = input("Enter table name: ")

a=""
while ( a != "e" ) :

    a = input("Enter field name or e for exit: ")
    if ( a != "e"):
        myList[0].append(a)

print("Your database " + tablename + " contains the following fields: ")
for j in myList[0] :
    print(j)

a = input("Add new instance?(y for yes)")
while(a == "y") :
    myList.append(list())
    i=i+1
    for j in myList[0]:
        myList[i].append(input(j+": "))
    a = input("Add new instance?(y for yes)")

t = PrettyTable(myList[0])
for j in myList:
    t.add_row(j)
t.del_row(0)
print(t)