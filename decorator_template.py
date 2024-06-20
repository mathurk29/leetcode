import functools


def decorator(func):
    """
    Extend functionality without modifying a function.
    """

    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Extend functionality here
        value = func(*args, **kwargs)
        # Extend functionality here
        return value

    return wrapper_decorator
