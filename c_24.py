'''
    Context Manager ith classes.

    You can deploy your own protocols only deploying dunder
    methods that Python will use.

    This is called Duck typing. It's a concept related with
    dinamic typing where python is not intested in the type,
    but if an method exists in its object to let it work
    in a good way.

    Duck typing:
    When I see a bird that walk like a duck, swim like
    a duck and quack like a duck, I call that bird as
    duck.

    To build a context manager, the methods __enter__ and
    __exit__ must be deployed.

    The __exit__ method will reveive the exeption class,
    the exception and traceback. If it returns TRUE, the
    exception in the with gonna be supressed.

'''

class MyOpen:
    def __init__(self, path, mode) -> None:
        self.path = path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('OPENING')
        self._file = open(self.path, self.mode, encoding='utf8') 
        return self._file


    def __exit__(self, class_exception, exception_, traceback_):
        print('CLOSING')
        self._file.close()

        #raise class_exception()
        if class_exception != None:
            print(class_exception)
            print(exception_)
            print(traceback_)

            return False

        return True # I dealt with the exception

instance = MyOpen('c_24.txt', 'w')



with instance as file:
    file.write('First line\n')
    print('WITH', file)


