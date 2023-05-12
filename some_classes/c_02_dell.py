# Decorator classes

from typing import Any


class DoMath:
    def __init__(self, func) -> None:
        self.func = func
        self._z = 10


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        result = self.func(*args, **kwds)
        
        return result * self._z


@DoMath
def do_sum(x, y):
    return x + y


result = do_sum(2, 5)
print(result)