#OOP Exercises

#Exercise R-2.4

class Flower:
    def __init__(self,name,number,price):
        self._name = name
        self._number = number
        self._price = price

    def name(self):
        return self._name

    def number(self):
        return self._number

    def price(self):
        return self._price

if __name__ == '__main__':
    f = Flower("Tulip",4,5)
    print(f.name())

#R-2.9 and R.10
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

    def __sub__(self,other):
        if len(self) != len(other):
            raise ValueError('the dimensions are not equal ')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j]*-1
        return result

    def __eq__(self,other):
        return self._coords == other._coords

    def __ne__(self,other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'