# Relationship between classes: association, agrgation and composition
# Association is a type of relationship where the objects are linked inside the system
# This relationship is the most comumn between and has subgroups wwith agregation and composition.
# Usualy, we have an association when the object has one attibute which is liked to another object
# An association doesn't manage how an object control the life cicle of another object.

class Writer:
    def __init__(self, name):
        self.name = name
        self._instrument = None
    
    @property
    def instrument(self):
        return self._instrument
    
    @instrument.setter
    def instrument(self, instrument):
        self._instrument = instrument
    

class WriteInstrument:
    def __init__(self, name):
        self.name = name
    

    def write(self):
        return f'{self.name} is writing'

writer = Writer("luiz")
pen = WriteInstrument('pen')

writer.instrument = pen

print(pen.write())
print(writer.instrument.write())
