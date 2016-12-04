from dataAccess import dataAccess as DB
import dateTime as DT

#path to filled out Database that has already been created with patient information from the provided CSVs
dbpath = “lab.db”

#connect to the Database by creating an instance of dataAccess
melDB = DB(“Melissa”, dbpath)

#values dictionary would look like this
values = [{\"1465778389\": 666}, {\"1465777482\":670}, {\"1465778681\": 690}]

#call the function on the Melissa table to create a new column
melDB.addcolumn(““slope””, values) 
