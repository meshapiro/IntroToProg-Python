
# This file is the minimal code needed to experiment with a different way to remove an item from the list
# Which I found in a classmate's repo
# I like it more than what I have now but haven't been able to make it work in my full program


# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
objFile = None   # File handle
strData = ""     # A row of text data from the file
dicRow = {}      # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []    # A list that acts as a 'table' of rows
strMenu = ""     # A menu of user options
strChoice = ""   # A user selected option
strTask = ""     # A task to be entered by the user if they choose to do so
strPriority = "" # A priority to be entered by the user if they choose to do so
strRemoveTask = "" # A task to be removed from the to-do list
blnTaskRemoved = False # A boolean value indicating whether a task has been removed

# -- Processing -- #
# Step 1 - When the program starts, load any data you have in a text file called ToDoList.txt
# into a python list of dictionaries rows (like Lab 5-2)

#open the file and read - option "r"
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()} #turn each row of the file into a dictionary
    lstTable.append(dicRow) #add each dictionary on as a row to lstTable
objFile.close()

    # Step 5 - Remove a new item from the list/Table
for dicRow in lstTable:
    print(dicRow["Task"] + ", " + dicRow["Priority"])  # Loop through and print the elements of each dictionary row

strRemoveTask = input("Enter the name of the task you wish to cross off: ") #User specifies which task to remove
for row in lstTable:
            if row['Task'].lower() == strRemoveTask.lower():
                lstTable.remove(row)
                print('Task has been removed: ' + strRemoveTask)
for dicRow in lstTable:
    print(dicRow["Task"] + ", " + dicRow["Priority"]) #Loop through and print the elements of each dictionary row
