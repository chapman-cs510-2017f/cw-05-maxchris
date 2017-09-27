#!/usr/bin/env python3

# Name: Maksym Solodovskyi & Chris Watkins
# Student ID:  & 1450263
# Email:  & watki115@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 5
###

from abscplane import AbsComplexPlane
class ListComplexPlane(AbsComplexPlane):
    def __init__(self, xmin, xmax, xlen, ymin, ymax, ylen):
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen
        # The implementation type of plane is up to the user
        self.plane = []
        # fs should be a list of functions, initialized to be empty
        self.fs = []

    def refresh(self):
        plane = []
        planex = []
        planey = []
        x = self.xmin
        y = self.ymin
        n= self.xlen
        m = self.ylen
        dx = (self.xmax - self.xmin)/(n-1)
        dy = (self.ymax - self.ymin)/(m-1)
        for i in range(n):
            for j in range (m):
                plane.append(x+i*dx+((y+j*dy)*1j))
        return plane
        """Regenerate complex plane.
        Populate self.plane with new points (x + y*1j), using
        the stored attributes of xmax, xmin, xlen, ymax, ymin,
        and ylen to set plane dimensions and resolution. Reset
        the attribute fs to an empty list so that no functions 
        are transforming the fresh plane.
        """
        

       
    
    def apply(self, f):
        self.f = f
        self.fs.append(f)
        newplane = []
        newplanex = []
        newplaney = []
        shiftxmin = self.xmin + f[0]
        shiftymin = self.ymin + f[1]
        shiftxmax = self.xmax + f[0]
        shiftymax = self.ymax + f[1]
        n = self.xlen
        m = self.ylen
        for i in range (shiftxmin, shiftxmax):
            
            newplanex.append(i)
            i+=(self.xmax - self.xmin)/(n-1)
        for j in range (shiftymin, shiftymax):
            newplaney.append(j)
            j+= (self.ymax - self.ymin)/(m-1) 
        newplane.append(newplanex)
        newplane.append(newplaney)
        return newplane
        
        """Add the function f as the last element of self.fs. 
        Apply f to every point of the plane, so that the resulting
        value of self.plane is the final output of the sequence of
        transformations collected in the list self.fs.
        """
        
    
    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen
        
        for i in range (0,len(f)):
            plane.self.fs.apply(f(i))
        return plane
    
        """Reset self.xmin, self.xmax, and self.xlen.
        Also reset self.ymin, self.ymax, and self.ylen.
        Regenerate the plane with the new range of the x- and y-axes,
        then apply all transformations in fs in the correct order to
        the new points so that the resulting value of self.plane is the
        final output of the sequence of transformations collected in
        the list self.fs."""
        
P = ListComplexPlane(1,5,5,1,5,5)
print(P.refresh())

