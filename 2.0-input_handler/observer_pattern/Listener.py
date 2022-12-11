from typing import Any

# The class Listener is the observer interface.

class Listener:
    def on_input(input_id: str, event: Any) -> None:
        raise NotImplementedError()
