'''

    Metaclasses are one type of classes

    In Python, everything is a object (class al well)

    So, what is the class type?

    Your object is a class instance

    Your class is a type instance (type is a metaclass)

    type ('Name', (Bases,), __dict__)

    When you create a class, things happen by standard
    in this order:
    __new__ of the metaclass is called and create a new class.
    __call__ of the metaclass is called with the parameters and call:
        __new__ of the class with the parameters (create an instance)
        __init__ of the class with the parameters
    __call__ of the metaclass finish the execution.


    Main methods of the metaclass:

    __new__(mcs, name, bases, dct) (Create a class)
    __cal__(cls, *args, **kwargs) (Create and initialize the instance)


    'Metaclasses are magic things deeper than 99% of the users
    should care of. If you want to know if you need them, you don't need
    (people that really need them know with certain that need them and
    don't ask for a explanation about the reason).'
    - Tim Peters (CPython Core Developer)

'''

from typing import Any


def my_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('Meta new')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = my_repr

        return(cls)
    
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        instance = super().__call__(*args, **kwds)
        print(instance.__dict__)
        
        if 'name' not in instance.__dict__:
            raise NotImplementedError('Create name')
        
        return instance


class Person(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('My new')
        instance_ = super().__new__(cls)

        return instance_
    

    def __init__(self, name) -> None:
        print('My init')
        self.name = name


p = Person('Gus')
print(p.attr)
print(p)