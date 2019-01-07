# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:36:26 2018

@author: 612436198
"""

from MovingShapes import *
frame = Frame()
numshapes = 3
shapes = []
for i in range(numshapes):
    shapes.append(Square(frame, 100))
    shapes.append(Diamond(frame, 100))
    shapes.append(Circle(frame, 100))
for i in range(100):
    for shape in shapes:
        shape.moveTick()
