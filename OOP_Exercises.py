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

#