"""
ISPPV1 2024
Anonymous Functions

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains an example of passing a lambda function
as an argument to a higher-level function with variadic arguments.
"""

from typing import Callable, Any


def higher_order_function(f: Callable, *args: tuple, **kwargs: dict) -> Any:
    print(f"Executing f({args}, {kwargs})")
    return f(*args, **kwargs)


result = higher_order_function(lambda x, y: x**y, 2, 3)
print(result)

result = higher_order_function(lambda a, b, c: a * b + c, 1, 2, 3)
print(result)

result = higher_order_function(lambda a, b, c: a * b + c, a=1, c=2, b=3)
print(result)
