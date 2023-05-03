# Simple inheritance - Relation between classes
# Association - uses, agregation, has
# Composition - Is the owner of, Inheritance - Is one
#
#
# Inheritance vs Composition
#
# Principal class (Person)
#   -> super class, base class, parent class
# Son class (Custumer)
#   -> sub class, child class, derived class

# object is a built-in that will give her inheritance to the classes
class Foo(object):
    ...

#help(Foo)

class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    
    def print_class_name(self):
        print(self.__class__.__name__)

class Custumer(Person):
    ...

c1 = Custumer('Luiz', 'Otávio')
#print(c1.name, c1.last_name)
#c1.print_class_name()

p1 = Person("Gus", "Tavo")
#p1.print_class_name()
#print(p1.name, p1.last_name)

#help(c1)
'''
Help on Custumer in module __main__ object:

class Custumer(Person)
 |  Custumer(name, last_name)
 |
 |  Method resolution order:
 |      Custumer
 |      Person
 |      builtins.object
 |
 |  Methods inherited from Person:
-- More  --
'''

class MyString(str):
    def upper(self):
        print(self)
        return_to = super().upper()
        return return_to


string = MyString('Luiz')
#print(string.upper())


########################################################


