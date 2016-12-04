#Step 0: import the dataAccess file and dateTime
from dataAccess import dataAccess as DB
import dateTime as DT

#Step 1: specify the path to the database file 
###path to filled out Database that has already been created with patient information from the provided CSVs
dbpath = “lab.db”

#Step 2: Connect to that database and create an instance of dataAccess
###connect to the Database by creating an instance of dataAccess
melDB = DB(“Melissa”, dbpath)

#Step 3: Create a dictionary that has the times and values that need to be added to the new column
###values dictionary would look like this
values = [{\"1465778389\": 666}, {\"1465777482\":670}, {\"1465778681\": 690}]

#Step 4: Call the function by passing a name for the column and the dictionary of values
###call the function on the Melissa table to create a new column
melDB.addcolumn('“slope”', values) 

