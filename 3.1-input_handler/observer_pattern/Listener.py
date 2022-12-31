"""
ISPPJ1 2023
Input handler by observers.

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Listener, the observer interface.
"""
from typing import Any


class Listener:
    def on_input(input_id: str, event: Any) -> None:
        raise NotImplementedError()
