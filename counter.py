import functools
from dataclasses import dataclass

# from builtins import function


class Counter:

    def __init__(self, i: int = 0):
        self.val = i

    def add(self):
        self.val += 1

    def sub(self):
        self.val -= 1


c = Counter()


def with_counter(f):
    """
    adds 1 to counter when function is
    :param f:
    :return:
    """

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        c.add()
        print(c.val)
        f(*args, **kwargs)
        c.sub()
        print(c.val)

    return wrapper


def generate():
    """
    keep track of number of functions created
    :return:
    """

    @with_counter
    def fn():
        pass

    return fn
