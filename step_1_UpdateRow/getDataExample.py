from dataAccess import dataAccess as DB
import dateTime as DT


#path to filled out Database that has already been created with patient information from the provided CSVs


dbpath = “lab.db”


#connect to the Database by creating an instance of dataAccess
melDB = DB(“Melissa”, dbpath)


#call the function on the Melissa table which will return all of the data in the database for Melissa
print(melDB.getData())
