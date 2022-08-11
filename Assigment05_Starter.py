# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot, 1.1.2030,Created started script
# MShapiro, 8/7/22, Filled in code for all but Step 5 - remove an item
# MShapiro, 8/10/22, Followed along with solution video to create Step 5
# ------------------------------------------------------------------------ #

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

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Here is your current to-do list: ")
        for dicRow in lstTable:
            print(dicRow["Task"] + ", " + dicRow["Priority"]) #Loop through and print the elements of each dictionary row
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter a task: ") #Take user data for new task and priority
        strPriority = input("Enter the task's priority level [Low, Medium, High, or Urgent]: ")
        dicRow = {"Task":strTask, "Priority":strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemoveTask = input("Enter the name of the task you wish to cross off: ") #User specifies which task to remove
        intRowNum = 0 #starting with the 1st row (0 position)
        while intRowNum < len(lstTable):
            #For each row of lstTable, compare the task to be removed
            #with the first element of each row (which will correspond to the task)
            if (strRemoveTask.lower() == str(list(dict(lstTable[intRowNum]).values())[0]).lower()):
                del lstTable[intRowNum] #if comparison returns True, delete the corresponding row
                blnTaskRemoved = True #and set the boolean for removed to True
            intRowNum += 1 #Increase the counter to check the next row
        if (blnTaskRemoved == True):
            print("You completed task: \"" + strRemoveTask + "\" - Nice job!")
        else:
            print("No task by that name in your list!")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        if('y' == str(input("Do you want to save this data? y/n ")).strip().lower()):
            objFile = open(strFile, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + ',' + dicRow["Priority"] + '\n') #write each element in each dictionary row to file
            objFile.close()
            input("Data saved to to-do list file. Press ENTER to return to menu.")
        else:
            input("Data not saved to file. Data is still in program's working memory. Press ENTER to return to menu.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exiting program. Goodbye!")
        break  # and Exit the program
