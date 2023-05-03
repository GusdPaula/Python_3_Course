# @property is a getter in a pytonic mode
# getter is a mathod to get an attribute
# pytonic mode is the way which python do things
# @property is an object property, it is a method that 
# work as an attribute
# Usualy it is used in the below situations:
# ---- As a getter
# ---- To don't allow the code breaking for a client code
# ---------- Client code is a code that uses your code
# ---- To allow a setter
# ---- To run actions to get an attribute
# Attributes that begin with one or more unserscore don't should be used outside the class

class Pen:
    def __init__(self, color):
        self._color = color

    @property
    def get_color(self):
        return self._color
    

    @get_color.setter
    def color(self, value):
        self._color = value


blue_pen = Pen('blue')
print(blue_pen.get_color)

blue_pen.color = "red"
print(blue_pen.get_color)