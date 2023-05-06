# Decorators functions and decoraters with classes

def add_repr(cls):
    def my_repr(self) -> str:
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'

        return class_repr

    cls.__repr__ = my_repr

    return cls

def my_planet(method):
    def intern(self, *args, **kwarwgs):
        result = method(self, *args, **kwarwgs)

        if 'Earth' in result:
            return 'You are in home!'

        return result
    return intern


@add_repr
class Team():
    def  __init__(self, name) -> None:
        self.name = name


@add_repr
class Planet():
    def __init__(self, name) -> None:
        self.name = name

    @my_planet
    def speak_name(self):
        return f'The name is {self.name}'


brazil = Team('Brazil')
portugal = Team('Portugal')

earth = Planet('Earth')
mars = Planet('Mars')

print(brazil)
print(portugal)

print(earth)
print(mars)

print(mars.speak_name())
print(earth.speak_name())