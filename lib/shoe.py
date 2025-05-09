#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand=brand
        self.size=size
        self.condition = "Old"

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,size):
        if not isinstance(size, int):
            print("size must be an integer")

        else:
            self._size=size

    def cobble(self):
        self.condition="New"
        print("Your shoe is as good as new!")




shoe = Shoe("Adidas", 38)
print(shoe.size)
print(shoe.condition)  # Old
shoe.cobble()          # prints: Your shoe is as good as new!
print(shoe.condition)  # New


    
