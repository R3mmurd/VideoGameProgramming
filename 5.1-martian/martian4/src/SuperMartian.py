import pygame

from gale.game import Game
from gale.state_machine import StateMachine

from src.states import game_states

class SuperMartian(Game):
    def init(self) -> None:
        self.state_machine = StateMachine({
            'play': game_states.PlayState
        })
        self.state_machine.change('play')
    
    def update(self, dt: float) -> None:
        self.state_machine.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        self.state_machine.render(surface)
