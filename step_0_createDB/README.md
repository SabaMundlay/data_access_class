
##Step 0: import appropriate libraries
from dataAccess import dataAccess as DB
import datetime as dt
import glob
import os.path
import sys

##Step 1: create database file (if '.db' file does not exist, 'dbpath=' will create one)
dbpath = "lab.db"
datapath = "Kate_G5_June13_Sept10_2016.csv"
pidMelissa = "Kate"

##Step 2: Connect to the Database by creating an instance of dataAccess
db = DB(pidKate, dbpath)

##Step 3: Insert data into database
db.insertData(datapath)
