# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:12:29 2019

@author: 612436198
"""

#Task 1: Create a table and insert data.

import sqlite3

conn = sqlite3.connect("task1.db")

c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

#The caps aren't strictly necessary but are to help distinguish SQL-related commands from other things like table and column names.
#stuffToBuild = the database table name
#unix, datestamp, keyword and value are the column names in the database table. You can define any names you like, and put them in lowercase.
#REAL and TEXT are the data types and format in each column, which are also SQL language, so are in uppercase.

def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(142233222, '2018-01-01', 'python', 5)")
    conn.commit()
    c.close()
    conn.close()
    
#You created a four-column table, so need four bits of data when inputting.
#When you run the two functions above, a new database file will be created, with the inputted data in it. Needs to be opened with a database browser.

#Task 2: Add data to your table with variables.

import sqlite3
import time
import datetime
import random

conn = sqlite3.connect("task1.db")
c = conn.cursor()

def dynamic_data_entry():
    unix = time.time()
    datestamp = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S"))
    keyword = "Python"
    value = random.randrange(0, 10)
    c.execute("INSERT INTO stuffToBuild(unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)", (unix, datestamp, keyword, value))
    conn.commit()
 
#In the c.execute line in the function above, the first 'unix, datestamp, keyword, value' represents the columns, the second represets the variables.   

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
    
c.close()
conn.close()

#Task 3: Read and select data from a database.

#The SELECT command in in SQL is use to only read the data clumns based on your choice, and SELECT * means to select all the columns in the data table.
#Usually, after nominating the selected data columns, there is a FROM command that point to which data table you should select from. This is because one database can contain multiple database tables.
#A WHERE clause is used for further filtering the data inside each column.

def read_from_db_all():
    c.execute("SELECT * FROM stuffToBuild WHERE value = 8")
    for row in c.fetchall():
        print(row)
        
def read_from_db2():
    c.execute("SELECT * FROM stuffToBuild WHERE value = 8 and unix > 1547027961 and unix < 1547028085")
    for row in c.fetchall():
        print(row[0])
        
def read_from_db_using_select():
    c.execute("SELECT value FROM stuffToBuild WHERE unix < 1547027966")
    for row in c.fetchall():
        print(row)