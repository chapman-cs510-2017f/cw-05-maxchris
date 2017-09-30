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
    """   
        Attributes:
        xmax (float) : maximum horizontal axis value
        xmin (float) : minimum horizontal axis value
        xlen (int)   : number of horizontal points
        ymax (float) : maximum vertical axis value
        ymin (float) : minimum vertical axis value
        ylen (int)   : number of vertical points
        plane        : stored complex plane implementation
        fs (list[function]) : function sequence to transform plane
    """ 

    def refresh(self):
        self.plane = []
        self.fs = []
        x = self.xmin
        y = self.ymin
        n= self.xlen
        m = self.ylen
        dx = (self.xmax - self.xmin)/(n-1)
        dy = (self.ymax - self.ymin)/(m-1)
        for i in range(n):
            for j in range(m):
                self.plane.append(x+i*dx+((y+j*dy)*1j)) #Builds complex plane
        return self.plane
        """Regenerate complex plane.
        Populate self.plane with new points (x + y*1j), using
        the stored attributes of xmax, xmin, xlen, ymax, ymin,
        and ylen to set plane dimensions and resolution. Reset
        the attribute fs to an empty list so that no functions 
        are transforming the fresh plane.

        Returns:
            Complex plane after generating points.
        """
        
    def apply(self, f):
        plane_x =[]
        plane_y =[]
        self.f = f
        self.fs.append(self.f)
        for i in range(len(self.plane)): #Makes a list of the real and imaginary parts of points in the complex plane
            plane_x.append(self.plane[i].real)
            plane_y.append(self.plane[i].imag)
        plane_r =[plane_x, plane_y]
        n = len(plane_r[0])
        for i in range(len(plane_r)):
            for j in range(n):
                plane_r[i][j]= f(plane_r[i][j]) #Applies the function to the real and complex parts of points 
        plane_r[1]= [plane_r[1][j]*1j for j in range(n)] 
        self.plane = [sum(x) for x in zip(plane_r[0],plane_r[1])] #Puts the values together to get a complex number 
        return self.plane
        
        """Add the function f as the last element of self.fs. 
        Apply f to every point of the plane, so that the resulting
        value of self.plane is the final output of the sequence of
        transformations collected in the list self.fs.
        
        Args:
            f(func): Function
            
        Returns:
            Complex plane after applying the function.
        """
        
    
    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        self.plane = []
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen
        x = self.xmin
        y = self.ymin
        n= self.xlen
        m = self.ylen
        dx = (self.xmax - self.xmin)/(n-1)
        dy = (self.ymax - self.ymin)/(m-1)
        for i in range(n):
            for j in range(m):
                self.plane.append(x+i*dx+((y+j*dy)*1j)) #Builds complex plane from new attributes.
        for i in range(len(self.fs)):
            self.apply(self.fs[i]) #Applies all functions in order.
        return self.plane
    
        """Reset self.xmin, self.xmax, and self.xlen.
        Also reset self.ymin, self.ymax, and self.ylen.
        Regenerate the plane with the new range of the x- and y-axes,
        then apply all transformations in fs in the correct order to
        the new points so that the resulting value of self.plane is the
        final output of the sequence of transformations collected in
        the list self.fs.
        
        Args:
            xmax(float) : maximum horizontal axis value
            xmin(float) : minimum horizontal axis value
            xlen(int)   : number of horizontal points
            ymax(float) : maximum vertical axis value
            ymin(float) : minimum vertical axis value
            ylen(int)   : number of vertical points
        
        Returns:
            Complex plane after reinitializing the attributes and applying the functions. 
        """

    


