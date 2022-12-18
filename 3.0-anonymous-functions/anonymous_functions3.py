from typing import Callable, Any

def powerup(f: Callable) -> Callable:
    def f_with_steroids(*args, **kwargs) -> Any:
        print("Steroids for f")
        return f(*args, **kwargs)
    return f_with_steroids

f = powerup(lambda x, y: x ** y)
result = f(2, 3)
print(result)

@powerup
def my_f(x, y):
    return x ** y

result = my_f(2, 4)
print(result)
