# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Place:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    
    def __str__(self) -> str:
        return f'{self.x}, {self.y}'
    

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name=}({self.x=}, {self.y=})'
    

    def __add__(self, other):
        '''
            This will help with '+' below.

        '''
        
        new_x = self.x + other.x
        new_y = self.y + other.y

        return Place(new_x, new_y)
    

    def __gt__(self, other):
        '''
            This will help with '>' or '<' below.
        
        '''

        sum_self = self.x + self.y
        sum_other = other.x + other.y

        return sum_self > sum_other
            
    

p1 = Place(1, 2)
p2 = Place(55, 89)

print(p1)
print(p2)

# 3 ways to get the repr
print(p1.__repr__())
print(repr(p2))
print(f'{p2!r}')

p3 = p1 + p2

print(p3)

print(p1 < p2)