# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Seb Clendenning, 12.11.2022, Added code for Step 1 and Step 3
# Seb Clendenning, 12.12.2022, Added code for Step 4
# Seb Clendenning, 14.12.2022, Added code for Step 5 and Step 6
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {'Task', 'Priority'}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # Captures the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
readFile = open(objFile, 'r')
for row in readFile:
    lstRow = row.split(',')
    dicRow = {'Task':lstRow[0].strip(), 'Priority':lstRow[1].strip()}
    lstTable.append(dicRow)
readFile.close()
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
    strChoice = str(input("Which option would you like to perform? [1 to 5]: "))
    print('\n')  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print(row) # prints loaded in data to user
            continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        userTask = input("Add a new task: ")
        taskPriority = input("Add the task's priority (High, Medium, Low): ")
        dicRow = {'Task':userTask, 'Priority':taskPriority}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strInput = input("Input Task Name to remove it: ")
        for row in lstTable:
            if row['Task'].lower() == strInput.lower():
                lstTable.remove(row)
                print("Task has been removed.")
                print(lstTable) # print updated table to show task has been removed
                continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        writeFile = open(objFile, 'w')
        for row in lstTable: # loop through each row and write each task and priority to .txt file
            writeFile.write(row['Task'] + ', ' + row['Priority'] + '\n')
            continue
        print("Tasks have been saved to file.")
        writeFile.close() # closes the file
        # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
