# Class attribute
class Person:
    attribute = 2022

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def get_birth_year(self):
        return Person.attribute - self.age
    

p1 = Person("João", 35)

print(p1.get_birth_year())

# __dict__ and vars for ainstance attributes
print(p1.__dict__) # Take care, because you can edit with it.
print(vars(p1))

p1.__dict__['name'] = 'Jose'
print(p1.__dict__)

# Unpacking inside the class

p2 = Person(**p1.__dict__)
p1.__dict__['name'] = 'Joao'

print(vars(p2))
print(vars(p1))

# ---------------------------------------------------- #
#                   Saving as JSON                     #
# ---------------------------------------------------- #

import json

people = [p1.__dict__, p2.__dict__]

with open('my_class.json', 'w') as f:
    json.dump(people, f, ensure_ascii=False, indent=2)

del people

# ---------------------------------------------------- #
#                  Reloading the class                 #
# ---------------------------------------------------- #

with open('my_class.json', 'r') as f:
    people = json.load(f)

p3 = Person(**people[0])
p4 = Person(**people[1])

print("Reloaded data...")
print(vars(p3))
print(vars(p4))