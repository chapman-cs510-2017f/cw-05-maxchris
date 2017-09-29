#!/usr/bin/env python3

# Name: Maksym Solodovskyi & Chris Watkins
# Student ID: 2299101 & 1450263
# Email:  solodovs@chapman.edu & watki115@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 5
###

from cplane import ListComplexPlane

def test_cplane1():
    P = ListComplexPlane(1,2,2,1,2,2)
    assert P.refresh() == [(1+1j), (1+2j), (2+1j), (2+2j)]
    
def test_cplane2():
    P = ListComplexPlane(1,2,2,1,2,2)
    P.refresh()
    assert P.apply(lambda x:x+2) == [(3+3j), (3+4j), (4+3j), (4+4j)]
    
def test_cplane3():
    
    
    