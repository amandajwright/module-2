# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:13:32 2019

@author: amand
"""

import sqlite3

conn = sqlite3.connect("task1.db")

c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS phoneBook(firstName TEXT, lastName TEXT, addressLine1 TEXT, city TEXT, postcode TEXT, telephoneNumber TEXT, businessCategry TEXT, xCoordinate REAL, yCoordinate REAL)")