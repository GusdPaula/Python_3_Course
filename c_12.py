# @staticmethod
# They are methods which are inside the class, 
# but without access to cls or self.
# In summary, they are functions inside classes.

class Example:
    @staticmethod
    def function_inside_class():
        print("hello")

c1 = Example()

c1.function_inside_class()