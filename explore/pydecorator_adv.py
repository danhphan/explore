# AUTOGENERATED! DO NOT EDIT! File to edit: 10_pydecorator_adv.ipynb (unless otherwise specified).

__all__ = ['count_calls', 'fibonacci', 'CountCalls', 'fibonacci']

# Cell
import functools
def count_calls(func):

    """Count the number of calls to a function"""
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        _wrapper.num_calls += 1
        return value
    _wrapper.num_calls = 0
    return _wrapper


@count_calls
def fibonacci(number):
    """Calculate Fibonacci numbers fib_n
    The Fibonacci numbers are 1, 2, 3, 5 ,8, 12, 21, ...
        fib_n = fib_n-1 + fib_n-2
    """
    if number < 2: return 1
    return fibonacci(number-1) + fibonacci(number-2)

# Cell
# A class can be a decorator if it is callable (or it contains a __call__ function)
class CountCalls:
    """Count a number of calls for a function"""

    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        ...
        self.num_calls += 1
        return self.func(*args, **kwargs)

@CountCalls
def fibonacci(number):
    """Calculate Fibonacci numbers fib_n
    The Fibonacci numbers are 1, 2, 3, 5 ,8, 12, 21, ...
        fib_n = fib_n-1 + fib_n-2
    """
    if number < 2: return 1
    return fibonacci(number-1) + fibonacci(number-2)