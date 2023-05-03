# Building Exceptions in Python Object Oriented
# To build an Exeption in Python, you just
# need inherit some language exception;
# The doc recomendation is to inherit from Exception.
# Building comumn Exeptions (Put the error on the end)
# Raising / throwing
# Rereading exeptions
# Adding notes in exceptions

class MyError(Exception):
    ...


class AnotherError(Exception):
    ...


def to_raise():
    exception_ = MyError('My error mensage')
    exception_.add_note('Look the first note')
    exception_.add_note('You did wrong with it.')
    raise exception_

try:
    #a = 1/0
    to_raise()

except (MyError, ZeroDivisionError) as error:
    class_error_name = error.__class__.__name__
    class_error_msg = error
    print(f'{class_error_name=}')
    print(f'{class_error_msg=}')
    print(error.__notes__)
    print(error.args)

    #exception_ = AnotherError('Another error')

    #raise exception_