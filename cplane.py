#!/usr/bin/env python3

# Name: Maksym Solodovskyi & Chris Watkins
# Student ID: 2299101 & 1450263
# Email:  solodovs@chapman.edu & watki115@mail.chapman.edu
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
        self.fs = []
        x = self.xmin
        y = self.ymin
        n= self.xlen
        m = self.ylen
        dx = (self.xmax - self.xmin)/(n-1)
        dy = (self.ymax - self.ymin)/(m-1)
        for i in range(n):
            for j in range(m):
                plane.append(x+i*dx+((y+j*dy)*1j))
        self.plane = plane
        return plane
        """Regenerate complex plane.
        Populate self.plane with new points (x + y*1j), using
        the stored attributes of xmax, xmin, xlen, ymax, ymin,
        and ylen to set plane dimensions and resolution. Reset
        the attribute fs to an empty list so that no functions 
        are transforming the fresh plane.
        """
        
    def apply(self, f):
        plane = self.plane
        plane_x =[]
        plane_y =[]
        self.f = f
        self.fs.append(self.f)
        fs = self.fs
        for i in range(len(plane)):
            plane_x.append(plane[i].real)
            plane_y.append(plane[i].imag)
        plane_r =[plane_x, plane_y]
        n = len(plane_r[0])
        for k in range(len(fs)):
            for i in range(len(plane_r)):
                for j in range(n):
                    plane_r[i][j]= f(plane_r[i][j])
        plane_r[1]= [plane_r[1][j]*1j for j in range(n)]
        plane = [sum(x) for x in zip(plane_r[0],plane_r[1])]
        return plane
        
        """Add the function f as the last element of self.fs. 
        Apply f to every point of the plane, so that the resulting
        value of self.plane is the final output of the sequence of
        transformations collected in the list self.fs.
        """
        
    
    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        plane = self.plane
        fs = self.fs
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen
        self.refresh
        for i in range(len(fs)):
            self.apply(self.fs[i])
        self.plane = plane
        return plane
    
        """Reset self.xmin, self.xmax, and self.xlen.
        Also reset self.ymin, self.ymax, and self.ylen.
        Regenerate the plane with the new range of the x- and y-axes,
        then apply all transformations in fs in the correct order to
        the new points so that the resulting value of self.plane is the
        final output of the sequence of transformations collected in
        the list self.fs."""

    
P = ListComplexPlane(1,5,5,1,5,5)
P.refresh()
P.apply(lambda x:x+2)
#print(P.zoom(2,4,2,2,4,2))

