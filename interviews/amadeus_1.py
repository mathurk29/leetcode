def factorial(n):

    try:

        if n < 0:
            raise NameError
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)

    except NameError:
        return "Exception caught: n is -ve"


factorial(-5)


class Stack:
    def __init__(self) -> None:
        self.stack = list()

    def insert(self, val):
        self.stack.append(val)

    def pop(self):
        poped_item = self.stack.pop()
        print(poped_item)


stk = Stack()

stk.insert(0)
stk.insert(1)
stk.insert(2)
stk.insert(3)
stk.insert(4)
stk.insert(5)

stk.stack

stk.pop()


def outer(fn):
    def inner(*args, **kwargs):
        return summation(*args, **kwargs)
    return inner


@outer
def summation(a, b):
    return a + b


summation(10, 2)

summation(3, 6)
