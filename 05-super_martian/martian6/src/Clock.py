"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Clock.
"""

class Clock:
    def __init__(self, time: int) -> None:
        self.time = time
    
    def count_up(self) -> None:
        self.time += 1
    
    def count_down(self) -> None:
        self.time = max(0, self.time - 1)

    def __str__(self) -> str:
        return str(self.time)
