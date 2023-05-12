'''
Special method __call__

callable is something that can be executed with brackets

In normal classes, __cal__ does an instance of one
callable class.

'''

from typing import Any


class CallMe:
    def __init__(self, phone) -> None:
        self.phone = phone
    

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(args[0], 'Calling: ', self.phone)

call1 = CallMe('2121232')
call1('Gustavo')