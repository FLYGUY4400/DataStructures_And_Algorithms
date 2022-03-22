#Object Oriented Programming
#Date: 3/22/2022

#Single underscore implies that the data member is nonpublic

#Example: Multidimensional Vector Class
import copy


class Vector:
    """Represents a vector in a multidimensional space."""

    def __init__(self,d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0]*d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self,j):
        return self._coords[j]

    def __setitem__(self,j,val):
        self._coords[j] = val

    def __add__(self,other):
        if len(self) != len(other):
            raise ValueError('dimensions are not equal so we cannot add')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self,other):
        return self._coords == other._coords

    def __ne__(self,other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

#Iterators
#__next__ and __iter__ methods

#Inheritance
#class className(superclass)
#use super(). method to initialize an instance of a subclass

#Hierarchy of Numeric Progressions
#Arithmetic Progression and Geometric Progressions

"""
A metaclass offers a template for the class definition itself 
"""

"""
Namespaces and Object-Orientation 
A namespace is an abstraction that manages all of the identifiers that are defined in a particular scope 
"""

"""
Nested Classes:

"""

#Deep Copying

warmTones = ['orange' 'brown']

palette = copy.deepcopy(warmtones)