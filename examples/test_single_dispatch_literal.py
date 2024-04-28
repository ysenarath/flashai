from functools import singledispatchmethod
from typing import Literal


class A:
    @singledispatchmethod
    def f(self, arg: Literal[1]):
        return 100

    @f.register
    def _(self, arg: Literal[2]):
        return 200


if __name__ == "__main__":
    a = A()
    print(a.f(1))  # 100
    print(a.f(2))  # 200
    print(a.f(3))  # TypeError: Invalid argument type for A.f: 3
