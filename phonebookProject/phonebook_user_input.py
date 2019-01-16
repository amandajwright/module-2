# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 09:39:36 2019

@author: amand
"""

from phonebook_db_functions import *

search_type = input("Search for person or business?")
if search_type == "person":
    search_for_person()