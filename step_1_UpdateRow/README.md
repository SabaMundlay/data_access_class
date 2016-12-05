##Step 0:
from dataAccess import dataAccess as DB
import datetime as DT
dbpath="lab.db"

##Step 1: connect to the Database by creating an instance of dataAccess
kateDB = DB("Kate", dbpath)

##Step 2: datetime would look this this
at = DT.datetime.strptime("2016-06-13 00:04:38","%Y-%m-%d %H:%M:%S")

##Step 3: valueList would look like this
valueList = {"at": 2413, "carb": 204}

##Step 4: call the function on the Kate table with new data for the specific row
KateDB.updateRow(at, valueList)
