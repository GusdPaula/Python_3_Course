'''
    __new__ and __init in python classes.

    __new__ is the method responsible for create and 
    return the new object. It's why new receives cls.

    __new__ must return the new object.

    __init__ is the method responsible for run the
    instance. It's why init receives self.

    __init__ must return nothing (None).

    Object is the super class of one class.

'''

class A:
    def __new__(cls):
        instance = super().__new__(cls)
        instance.changed_attribute = "We can can change it"
        return instance
    

    def __init__(self) -> None:
        print("I'm the init")
    

    def __repr__(self) -> str:
        return 'A()'
    

class B(A):
    def __new__(cls, other_obj):
        instance = other_obj
        instance.changed_attribute = "Changed!"
        return instance
    

    def __init__(self, other_obj) -> None:
        self = other_obj
        print("I'm the init")
    

    def __repr__(self) -> str:
        return 'B()'
    

object_a = A()
print(object_a)
print(object_a.changed_attribute)
print('----------------------------')
object_b = B(object_a)
print(object_b.changed_attribute)
print(object_b)
