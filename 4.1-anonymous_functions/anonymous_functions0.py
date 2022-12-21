from typing import Callable, Any

def higher_order_function(f: Callable) -> Any:
    print("Executing f")
    return f()

result = higher_order_function(lambda: 10)
print(result)
