from typing import Callable

def create_print_the_value_of_i(i: int) -> Callable:
    def print_the_value_of_i() -> None:
        print(i)
    return print_the_value_of_i


fs = []

for i in range(5):
    fs.append(create_print_the_value_of_i(i))

for f in fs:
    f()
