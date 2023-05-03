# Class' methods
# They are methods where "self" será "cls", this is,
# instead of receive the instance as the first parameter,
# We will receive the class itself.

class Person:
    year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def class_method(cls):
        print("Hey")

    @classmethod
    def do_with_50(cls, nome):
        return cls(nome, 50)

p1 = Person("Joao", 34)
Person.class_method()
p2 = Person.do_with_50("Maria")

print(vars(p2))

print(p2.name)
