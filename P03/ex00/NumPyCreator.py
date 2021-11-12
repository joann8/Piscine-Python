from typing import Iterator
import numpy as np
from random import random

class NumPyCreator():

    @staticmethod
    def from_list(mylist):
        
        try:
            if not isinstance(mylist, list):
                raise TypeError("Error LIST : not a list")
            if isinstance(mylist[0], list) : #cas des nested listes
                for tmp in mylist:
                    if len(tmp) != len(mylist[0]):
                        raise TypeError("Error LIST : not the same size")                                     
            return np.array(mylist)
        except TypeError or ValueError:
            return None

    @staticmethod
    def from_tuple(mytup):
        try:
            if not isinstance(mytup, tuple):
                raise TypeError("Error TUPLE : not a tuple")
            if isinstance(mytup[0], tuple) : #cas des nested listes
                for tmp in mytup:
                    if len(tmp) != len(mytup[0]):
                        raise TypeError("Error TUPLE : not the same size")   
            return np.array(mytup)
        except TypeError:
            return None

    @staticmethod
    def from_iterable(myit):
        try:
            if not isinstance(myit, (list, tuple, Iterator)):
                raise TypeError("Error ITERABLE : not iterable")
            mylist = list(myit)
            if isinstance(mylist[0], list) :
                for tmp in mylist:
                    if len(tmp) != len(mylist[0]):
                        raise TypeError("Error ITERABLES : not the same size")                                     
            return np.array(mylist)
        except TypeError:
            return None

    @staticmethod
    def from_shape(myshape, value=0):
        try:
            if not isinstance(myshape, tuple):
                raise TypeError("Error SHAPE : not a tuple")          
            if not isinstance(myshape[0], int) or not isinstance(myshape[1], int) or myshape[0] < 0 or myshape[1] < 0:  
                raise TypeError("Error SHAPE : tuple values are not positive int")
            if value is not None and not isinstance(value , (int, float)):
                raise TypeError("Error SHAPE : not an int nor a float")                                   
            return np.array([[value for x in range(myshape[1])] for y in range(myshape[0])])
        except TypeError:
            return None

    @staticmethod
    def random(myshape):
        try:
            if not isinstance(myshape, tuple):
                raise TypeError("Error RANDOM : not a tuple")
            if not isinstance(myshape[0], int) or not isinstance(myshape[1], int) or myshape[0] < 0 or myshape[1] < 0:  
                raise TypeError("Error RANDOM : tuple values are not positive int")
            return np.array([[random() for x in range(myshape[1])] for y in range(myshape[0])])           
        except TypeError:
            return None        
    
    @staticmethod
    def identity(n):
        try:
            if not isinstance(n, int) or n < 0:
                raise TypeError("Error IDENTITY : n not a positive int")
            return np.identity(n)
        except TypeError:
            return None      
