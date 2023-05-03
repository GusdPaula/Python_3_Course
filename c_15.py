# Encapsulation (access modifiers: public, protected, private)
# Python doesn't have access modifiers
# But we can follow the below conventions
#------ Without underscore = public
#------------------- It can be accessed outside the class
#------ With one underscore = protected
#------------------- It shouldn't be used outside the class or subclasses
#------ With two underscores = private
#------------------- "Name Mangling" in python it should be used inside the class that it was declared.

class Foo:
    def __init__(self):
        self.public = "It's pubic"
        self._protected = "It's protected"
        self.__private = "It's private"

    
    def public_method(self):
        return 'public method'

    def _protected_method(self):
        return 'protected method'
    
    def __private_method(self):
        return 'private method'
    
    


