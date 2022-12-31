"""
ISPPJ1 2023
Anonymous Functions

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains an example of passing a lambda function
as an argument to a higher-level function.
"""
from typing import Callable, Any


def higher_order_function(f: Callable) -> Any:
    print("Executing f")
    return f()


result = higher_order_function(lambda: 10)
print(result)
