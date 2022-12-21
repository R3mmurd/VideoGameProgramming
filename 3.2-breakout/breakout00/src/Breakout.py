import pygame

from gale.game import Game
from gale.state_machine import StateMachine

class Breakout(Game):
    def init(self) -> None:
        self.state_machine = StateMachine()

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        self.state_machine.render(surface)
