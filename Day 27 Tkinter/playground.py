# Postitional arguments


def add(*args):
    Sum = 0
    for num in args:
        Sum += num
    return Sum


print(add(1, 2, 3))


# Keyword arguments


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(kwargs)


print(calculate(3, add=2, multiply=5))


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")  # get is better than indexing with []
        self.model = kwargs.get("model")
