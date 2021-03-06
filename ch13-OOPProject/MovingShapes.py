# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:42:40 2018

@author: 612436198
"""

from Shapes import *
from pylab import random as r
import math

class MovingShape:

    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.diameter = diameter
        self.frame = frame
        self.figure = Shape(shape, diameter)
        self.startDirection()
        self.minMax()
        self.x = self.minx + r() * (self.maxx - self.minx)
        self.y = self.miny + r() * (self.maxy - self.miny)

    def startDirection(self):
        randomNum = r()
        if r() > 0.5:
            self.dx = 5 + 10 * r()
            self.dy = 5 + 10 * r()
        else:
            self.dx = (5 + 10 * r()) * -1
            self.dy = (5 + 10 * r()) * -1
        return self.dx, self.dy
        
    
    def minMax(self):
        self.minx = self.diameter / 2
        self.miny = self.diameter / 2
        self.maxx = self.frame.width - self.minx
        self.maxy = self.frame.height - self.miny
        return self.minx, self.miny, self.maxx, self.maxy

    def shapeArea(self):
        area = self.diameter**2
        return area
    
    def goto(self, x, y):
        self.figure.goto(x, y)
        area = self.shapeArea()
        print("I am a {}, my area is {} and my centre point is at ({}, {})".format(self.shape, area, self.x, self.y))

    def moveTick(self):
        if self.x >= self.maxx or self.x <= self.minx:
            self.dx = -self.dx
        else:
            self.dx = self.dx
        
        if self.y >= self.maxy or self.y <= self.miny:
            self.dy = -self.dy
        else:
            self.dy = self.dy
        
        self.x = self.x + self.dx
        self.y = self.y + self.dy
 
        self.goto(self.x, self.y)
        
class Square(MovingShape):
     def __init__(self, frame, diameter):
         MovingShape.__init__(self, frame, "square", diameter)     
         
class Diamond(MovingShape):
     def __init__(self, frame, diameter):
         MovingShape.__init__(self, frame, "diamond", diameter)

     def minMax(self):
        self.minx = math.sqrt((self.diameter**2)*2) / 2
        self.miny = math.sqrt((self.diameter**2)*2) / 2
        self.maxx = self.frame.width - self.minx
        self.maxy = self.frame.height - self.miny
        return self.minx, self.miny, self.maxx, self.maxy

class Circle(MovingShape):
     def __init__(self, frame, diameter):
         MovingShape.__init__(self, frame, "circle", diameter)
         
     def shapeArea(self):
         area = math.pi * ((self.diameter / 2)**2)
         return area