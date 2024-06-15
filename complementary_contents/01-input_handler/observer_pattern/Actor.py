"""
ISPPJ1 2024
Input handler by observers.

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Actor, a Listener of input events.
"""

from typing import Any

from Listener import Listener


class Actor(Listener):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def on_input(self, input_id: str, event: Any) -> None:
        if input_id == "jump" and event.pressed:
            print(f"{self} is jumping")
        elif input_id == "shoot" and event.pressed:
            print(f"{self} is shooting")
        elif input_id == "rotate_left":
            print(f"{self} is rotating left")
        elif input_id == "rotate_right":
            print(f"{self} is rotating right")
        elif input_id == "rotate_up":
            print(f"{self} is rotating up")
        elif input_id == "rotate_down":
            print(f"{self} is rotating down")
