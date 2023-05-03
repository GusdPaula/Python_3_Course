# Abstractmethod for any method already decorated
# It's possible to create @property @property.setter @classethod
# @staticmethod and usual methods as abstracts, for this
# use @abstractmethod as decorator more inside
# Foo - Bar are words used as placeholder
# for words that can change in programing

from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name
        

    @property
    @abstractmethod
    def name(self):...


    @name.setter
    def name(self, name):...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        #print("Sou inútil")
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name)