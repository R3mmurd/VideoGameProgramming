import pygame

from gale.input_handler import InputHandler, InputData
from gale.state_machine import BaseState
from gale.text import render_text

import settings


class GameOverState(BaseState):
    def enter(self, score: int) -> None:
        self.score = score
        # A surface that supports alpha to draw behind the text.
        self.text_alpha_surface = pygame.Surface((424, 176), pygame.SRCALPHA)
        pygame.draw.rect(self.text_alpha_surface, (56, 56, 56, 234), pygame.Rect(0, 0, 424, 176))
        InputHandler.register_listener(self)

    def exit(self) -> None:
        InputHandler.unregister_listener(self)
    
    def render(self, surface: pygame.Surface) -> None:
        surface.blit(self.text_alpha_surface, (settings.VIRTUAL_WIDTH // 2 - 212, 24))
        render_text(surface, "GAME OVER", settings.FONTS['large'], settings.VIRTUAL_WIDTH // 2, 64, (99, 155, 255), center=True, shadowed=True)
        render_text(surface, f"Your Score: {self.score}", settings.FONTS['medium'], settings.VIRTUAL_WIDTH // 2, 140, (99, 155, 255), center=True, shadowed=True)
        render_text(surface, "Press Enter", settings.FONTS['medium'], settings.VIRTUAL_WIDTH // 2, 180, (99, 155, 255), center=True, shadowed=True)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == 'enter' and input_data.pressed:
            self.state_machine.change('start')
