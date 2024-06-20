# write a decorator to reverse a string


def outer(fn):

    def inner(*_, **kwargs):

        input = kwargs["input"]
        temp = ""
        i = len(input) - 1
        while i >= 0:
            temp += input[i]
            i -= 1

        return fn(temp)

    return inner


@outer
def test(input):
    return input


test(input="Mathur")
